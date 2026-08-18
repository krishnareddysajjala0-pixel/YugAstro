# -*- coding: utf-8 -*-
"""
Normalized Chart Context for YugAstro Results Engine.
Encapsulates native birth data, Lagna, 12 houses, 12 planet placements,
house lords, party affiliation, active Dasa/Antardasha, and transit state.
"""

import datetime
from typing import Dict, List, Any, Optional

LAGNA_ORDER = [
    "మేషం", "వృషభం", "మిథునం", "కర్కాటకం", "సింహం", "కన్య",
    "తులా", "వృశ్చికం", "ధనస్సు", "మకరం", "కుంభం", "మీనం"
]

GURU_PARTY_LAGNAS = ["మీనం", "మేషం", "కర్కాటకం", "సింహం", "వృశ్చికం", "ధనస్సు"]

GURU_PARTY_PLANETS = ["సూర్యుడు", "భూమి", "కుజుడు", "గురు", "కేతు", "చంద్రుడు"]

# Tritha Siddhantha 12-Planet Rulerships (Sign -> Lord)
SIGN_LORDS = {
    "మేషం": "కుజుడు",
    "వృషభం": "మిత్ర",
    "మిథునం": "చిత్ర",
    "కర్కాటకం": "చంద్రుడు",
    "సింహం": "సూర్యుడు",
    "కన్య": "బుధుడు",
    "తులా": "శుక్రుడు",
    "వృశ్చికం": "భూమి",
    "ధనస్సు": "కేతు",
    "మకరం": "రాహు",
    "కుంభం": "శని",
    "మీనం": "గురు"
}

class NormalizedChartContext:
    def __init__(self, data: Dict[str, Any], dasha_info: Optional[Dict[str, Any]] = None):
        self.raw_data = data
        self.raw_dasha = dasha_info or {}

        self.name: str = data.get('name', 'అనామకుడు')
        self.dob: str = data.get('dob', '')
        self.tob: str = data.get('tob', '')
        self.place: str = data.get('place', '')
        self.day_name: str = data.get('day_name', '')

        # Lagna info
        self.lagna: str = data.get('lagna', 'మేషం')
        self.lagna_index: int = LAGNA_ORDER.index(self.lagna) if self.lagna in LAGNA_ORDER else 0
        self.is_guru_party_lagna: bool = self.lagna in GURU_PARTY_LAGNAS

        # House mapping
        self.houses: Dict[str, int] = data.get('houses', {})
        self.house_signs: Dict[int, str] = {}
        for sign, h_num in self.houses.items():
            self.house_signs[int(h_num)] = sign

        # Ensure all 12 houses are present
        if not self.house_signs and self.lagna_index >= 0:
            for i in range(12):
                sign = LAGNA_ORDER[(self.lagna_index + i) % 12]
                self.houses[sign] = i + 1
                self.house_signs[i + 1] = sign

        # House Lords
        self.house_lords: Dict[int, str] = {}
        for h_num in range(1, 13):
            sign = self.house_signs.get(h_num, LAGNA_ORDER[(self.lagna_index + h_num - 1) % 12])
            self.house_lords[h_num] = SIGN_LORDS.get(sign, "సూర్యుడు")

        # Planet positions
        self.planet_positions: Any = data.get('planet_positions', {})
        self.planet_houses: Dict[str, int] = {}
        self.planet_signs: Dict[str, str] = {}
        self.planet_longitudes: Dict[str, float] = {}

        if isinstance(self.planet_positions, list):
            for item in self.planet_positions:
                if not isinstance(item, dict):
                    continue
                p_name = item.get('name', '')
                if not p_name or (p_name in self.planet_signs and item.get('is_hand')):
                    continue
                sign = item.get('lagna', '') or item.get('rasi', '')
                h_num = item.get('house', 0)
                lon = item.get('longitude', 0.0)

                if not h_num and sign in self.houses:
                    h_num = self.houses[sign]

                self.planet_signs[p_name] = sign
                self.planet_houses[p_name] = int(h_num) if h_num else 1
                self.planet_longitudes[p_name] = float(lon)

        elif isinstance(self.planet_positions, dict):
            for p_name, p_info in self.planet_positions.items():
                if isinstance(p_info, dict):
                    sign = p_info.get('rasi', '') or p_info.get('lagna', '')
                    h_num = p_info.get('house', 0)
                    lon = p_info.get('longitude', 0.0)
                else:
                    sign = str(p_info)
                    h_num = self.houses.get(sign, 1)
                    lon = 0.0

                if not h_num and sign in self.houses:
                    h_num = self.houses[sign]

                self.planet_signs[p_name] = sign
                self.planet_houses[p_name] = int(h_num) if h_num else 1
                self.planet_longitudes[p_name] = float(lon)

        # Lord Placements: house_num -> house where lord is placed
        self.lord_placements: Dict[int, int] = {}
        for h_num in range(1, 13):
            lord = self.house_lords[h_num]
            p_house = self.planet_houses.get(lord, 1)
            self.lord_placements[h_num] = p_house

        # Nakshatra info
        self.nakshatra: str = data.get('nakshatra', '')
        self.padam: int = data.get('padam', 1)
        self.nak_index: int = data.get('nak_index', 0)
        self.tithi_name: str = data.get('tithi_name', '')
        self.tithi_paksha: str = data.get('tithi_paksha', '')

        # Dasa info
        self.current_dasa: str = ""
        self.current_anthara: str = ""
        self.dasa_favorable: bool = True

        if isinstance(dasha_info, dict):
            self.current_dasa = dasha_info.get('current_dasa', '') or dasha_info.get('birth_dasa', '')
            self.current_anthara = dasha_info.get('current_anthara', '')
            
            all_dasas = dasha_info.get('all_dasas', [])
            for d in all_dasas:
                if d.get('is_current'):
                    self.current_dasa = d.get('maha', self.current_dasa)
                    self.dasa_favorable = d.get('is_favorable', True)
                    break

        if not self.current_dasa:
            self.current_dasa = data.get('birth_dasa', '')

    def get_party_for_planet(self, planet_name: str) -> str:
        return "GURU" if planet_name in GURU_PARTY_PLANETS else "SHANI"

    def is_favorable_planet(self, planet_name: str) -> bool:
        planet_party = self.get_party_for_planet(planet_name)
        lagna_party = "GURU" if self.is_guru_party_lagna else "SHANI"
        return planet_party == lagna_party

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'dob': self.dob,
            'tob': self.tob,
            'place': self.place,
            'lagna': self.lagna,
            'is_guru_party_lagna': self.is_guru_party_lagna,
            'house_signs': self.house_signs,
            'house_lords': self.house_lords,
            'planet_houses': self.planet_houses,
            'lord_placements': self.lord_placements,
            'nakshatra': self.nakshatra,
            'padam': self.padam,
            'current_dasa': self.current_dasa,
            'current_anthara': self.current_anthara,
            'dasa_favorable': self.dasa_favorable
        }

# -*- coding: utf-8 -*-
import astrology_data

attrs = [a for a in dir(astrology_data) if not a.startswith('_')]
print("astrology_data attributes:", attrs)

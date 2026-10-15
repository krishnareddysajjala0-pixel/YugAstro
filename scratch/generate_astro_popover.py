import json

# Read bhava_lord_rules.json
with open('bhava_lord_rules.json', 'r', encoding='utf-8') as f:
    bhava_lord_rules = json.load(f)

# Read planet_jyothishya_details.json
with open('planet_jyothishya_details.json', 'r', encoding='utf-8') as f:
    planet_details = json.load(f)

# Read house_jyothishya_details.json
with open('house_jyothishya_details.json', 'r', encoding='utf-8') as f:
    house_details = json.load(f)

bhava_lord_rules_js = json.dumps(bhava_lord_rules, ensure_ascii=False, indent=2)
planet_details_js = json.dumps(planet_details, ensure_ascii=False, indent=2)
house_details_js = json.dumps(house_details, ensure_ascii=False, indent=2)

js_template = f'''/**
 * YugAstro Interactive Graha & Bhava Karakatwalu Popover Engine
 * Based on Sri Sri Sri Acharya Prabodhananda Yogeeswarulu's
 * Thraitha Siddhantha "జ్యోతిష్య శాస్త్రము" & "12 భావ ఫలాలు"
 */
(function() {{
  'use strict';

  var PLANETS_DATA = {planet_details_js};

  var HOUSES_DATA = {house_details_js};

  var BHAVA_LORD_RULES = {bhava_lord_rules_js};

  var LAGNA_ORDER = [
    "మేషం", "వృషభం", "మిథునం", "కర్కాటకం",
    "సింహం", "కన్య", "తులా", "వృశ్చికం",
    "ధనస్సు", "మకరం", "కుంభం", "మీనం"
  ];

  var GURU_PARTY_LAGNAS = ["మేషం", "కర్కాటకం", "సింహం", "వృశ్చికం", "ధనస్సు", "మీనం"];
  var GURU_PARTY_PLANETS = ["సూర్యుడు", "చంద్రుడు", "కుజుడు", "గురువు", "గురు", "భూమి", "కేతు", "కేతువు", "రవి", "చంద్ర", "కుజ"];

  var OWN_HOUSE_RULES = {{
    "కుజుడు": "మేషం",
    "కుజ": "మేషం",
    "మిత్ర": "వృషభం",
    "చిత్ర": "మిథునం",
    "చంద్రుడు": "కర్కాటకం",
    "చంద్ర": "కర్కాటకం",
    "సూర్యుడు": "సింహం",
    "సూర్య": "సింహం",
    "రవి": "సింహం",
    "బుధుడు": "కన్య",
    "బుధ": "కన్య",
    "శుక్రుడు": "తులా",
    "శుక్ర": "తులా",
    "భూమి": "వృశ్చికం",
    "కేతు": "ధనస్సు",
    "కేతువు": "ధనస్సు",
    "రాహు": "మకరం",
    "రాహువు": "మకరం",
    "శని": "కుంభం",
    "గురువు": "మీనం",
    "గురు": "మీనం"
  }};

  var PLANET_STANDARD_DISPLAY = {{
    "కుజుడు": "కుజుడు",
    "కుజ": "కుజుడు",
    "మిత్ర": "మిత్ర",
    "చిత్ర": "చిత్ర",
    "చంద్రుడు": "చంద్రుడు",
    "చంద్ర": "చంద్రుడు",
    "సూర్యుడు": "సూర్యుడు",
    "సూర్య": "సూర్యుడు",
    "రవి": "సూర్యుడు",
    "బుధుడు": "బుధుడు",
    "బుధ": "బుధుడు",
    "శుక్రుడు": "శుక్రుడు",
    "శుక్ర": "శుక్రుడు",
    "భూమి": "భూమి",
    "కేతు": "కేతు",
    "కేతువు": "కేతు",
    "రాహు": "రాహు",
    "రాహువు": "రాహు",
    "శని": "శని",
    "గురువు": "గురువు",
    "గురు": "గురువు"
  }};

  var ALIASES_MAP = {{
    "రవి": "సూర్యుడు",
    "సూర్య": "సూర్యుడు",
    "sun": "సూర్యుడు",
    "ఇందు": "చంద్రుడు",
    "చంద్ర": "చంద్రుడు",
    "moon": "చంద్రుడు",
    "అంగారక": "కుజుడు",
    "కుజ": "కుజుడు",
    "mars": "కుజుడు",
    "సౌమ్య": "బుధుడు",
    "బుధ": "బుధుడు",
    "mercury": "బుధుడు",
    "బృహస్పతి": "గురువు",
    "గురు": "గురువు",
    "jupiter": "గురువు",
    "భృగు": "శుక్రుడు",
    "శుక్ర": "శుక్రుడు",
    "venus": "శుక్రుడు",
    "మంద": "శని",
    "శనిదేవుడు": "శని",
    "saturn": "శని",
    "ధూమకేతువు తల": "రాహువు",
    "రాహు": "రాహువు",
    "rahu": "రాహువు",
    "ధూమకేతువు తోక": "కేతువు",
    "కేతు": "కేతువు",
    "ketu": "కేతువు",
    "earth": "భూమి",
    "chitra": "చిత్ర",
    "mitra": "మిత్ర",
    "lagna": "లగ్నం",
    "ascendant": "లగ్నం"
  }};

  function normalizePlanetName(rawName) {{
    if (!rawName) return null;
    var clean = rawName.replace(/[🚩👉*⏱️()0-9°′'’\\s\\n\\r]+/g, '').trim();
    if (PLANETS_DATA[clean]) return clean;
    if (ALIASES_MAP[clean]) return ALIASES_MAP[clean];
    for (var k in PLANETS_DATA) {{
      if (clean === k || clean.indexOf(k) !== -1 || k.indexOf(clean) !== -1) return k;
    }}
    for (var a in ALIASES_MAP) {{
      if (clean === a || clean.indexOf(a) !== -1) return ALIASES_MAP[a];
    }}
    return null;
  }}

  // Vivarana Toggle State (Default: ENABLED)
  window.isVivaranaEnabled = function() {{
    var stored = localStorage.getItem('astro_vivarana_enabled');
    return stored !== 'false';
  }};

  window.toggleVivarana = function() {{
    var nextState = !window.isVivaranaEnabled();
    localStorage.setItem('astro_vivarana_enabled', nextState ? 'true' : 'false');
    window.updateVivaranaButtonUI();
    if (!nextState && popover) {{
      popover.style.display = 'none';
      if (hideTimeout) clearTimeout(hideTimeout);
    }}
  }};

  window.updateVivaranaButtonUI = function() {{
    var enabled = window.isVivaranaEnabled();
    var btns = document.querySelectorAll('#vivaranaToggleBtn, .top-btn-vivarana');
    btns.forEach(function(btn) {{
      if (enabled) {{
        btn.classList.add('active');
        btn.setAttribute('aria-pressed', 'true');
        btn.title = 'వివరణ ఆన్ చేయబడింది (క్లిక్ చేసి ఆఫ్ చేయవచ్చు)';
      }} else {{
        btn.classList.remove('active');
        btn.setAttribute('aria-pressed', 'false');
        btn.title = 'వివరణ ఆఫ్ చేయబడింది (క్లిక్ చేసి ఆన్ చేయవచ్చు)';
      }}
    }});
  }};

  function injectVivaranaStyles() {{
    if (document.getElementById('astro-vivarana-styles')) return;
    var style = document.createElement('style');
    style.id = 'astro-vivarana-styles';
    style.textContent = '.top-btn-vivarana {{ background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%) !important; border: 1px solid rgba(56, 189, 248, 0.6) !important; color: #ffffff !important; transition: all 0.2s ease !important; }} .top-btn-vivarana.active {{ opacity: 1 !important; background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%) !important; border: 1.5px solid #e0f2fe !important; box-shadow: 0 0 12px rgba(14, 165, 233, 0.6), 0 2px 8px rgba(0, 0, 0, 0.3) !important; }} .top-btn-vivarana:not(.active) {{ opacity: 0.55 !important; background: #334155 !important; border-color: #475569 !important; color: #94a3b8 !important; box-shadow: none !important; }}';
    document.head.appendChild(style);
  }}

  var popover = null;
  var hideTimeout = null;
  var currentTarget = null;

  function createPopover() {{
    if (popover) return popover;
    popover = document.createElement('div');
    popover.id = 'astro-interactive-popover';
    popover.style.cssText = [
      'position: fixed',
      'z-index: 999999',
      'max-width: 520px',
      'width: 94vw',
      'background: #0f172a',
      'color: #f8fafc',
      'border-radius: 12px',
      'box-shadow: 0 20px 40px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(255, 255, 255, 0.1)',
      'font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans Telugu", sans-serif',
      'font-size: 13px',
      'line-height: 1.55',
      'display: none',
      'overflow: hidden',
      'pointer-events: auto'
    ].join(';') + ';';

    popover.addEventListener('mouseenter', function() {{
      if (hideTimeout) clearTimeout(hideTimeout);
    }});
    popover.addEventListener('mouseleave', function() {{
      scheduleHide(200);
    }});

    document.body.appendChild(popover);
    return popover;
  }}

  function scheduleHide(delay) {{
    if (hideTimeout) clearTimeout(hideTimeout);
    hideTimeout = setTimeout(function() {{
      if (popover) {{
        popover.style.display = 'none';
        currentTarget = null;
      }}
    }}, delay || 200);
  }}

  function positionPopover(targetEl, clientX, clientY) {{
    if (!popover) return;
    popover.style.display = 'block';
    popover.style.visibility = 'hidden';

    var rect = targetEl ? targetEl.getBoundingClientRect() : null;
    var popWidth = popover.offsetWidth || 460;
    var popHeight = popover.offsetHeight || 340;
    var viewWidth = window.innerWidth;
    var viewHeight = window.innerHeight;

    var left, top;

    if (rect) {{
      left = rect.left + (rect.width / 2) - (popWidth / 2);
      if (rect.top - popHeight - 10 > 10) {{
        top = rect.top - popHeight - 10;
      }} else if (rect.bottom + popHeight + 10 < viewHeight) {{
        top = rect.bottom + 10;
      }} else {{
        top = Math.max(10, Math.min(viewHeight - popHeight - 10, rect.top));
        if (rect.left - popWidth - 10 > 10) {{
          left = rect.left - popWidth - 10;
        }} else {{
          left = rect.right + 10;
        }}
      }}
    }} else {{
      left = clientX - (popWidth / 2);
      top = clientY - popHeight - 10;
      if (top < 10) top = clientY + 16;
    }}

    if (left < 10) left = 10;
    if (left + popWidth > viewWidth - 10) left = viewWidth - popWidth - 10;
    if (top < 10) top = 10;
    if (top + popHeight > viewHeight - 10) top = viewHeight - popHeight - 10;

    popover.style.left = Math.round(left) + 'px';
    popover.style.top = Math.round(top) + 'px';
    popover.style.visibility = 'visible';
  }}

  // Determine the Lagna of the current chart
  function getChartLagna(targetEl) {{
    if (targetEl) {{
      var wrap = targetEl.closest('[data-chart-lagna], [data-lagna]');
      if (wrap) {{
        var l = wrap.getAttribute('data-chart-lagna') || wrap.getAttribute('data-lagna');
        if (l && LAGNA_ORDER.indexOf(l.trim()) !== -1) return l.trim();
      }}
    }}
    if (window.CHART_LAGNA && LAGNA_ORDER.indexOf(window.CHART_LAGNA.trim()) !== -1) {{
      return window.CHART_LAGNA.trim();
    }}
    var lagnaBox = document.querySelector('.box.lagna, .nak-box.lagna-box, [data-is-lagna="true"]');
    if (lagnaBox) {{
      var r = lagnaBox.getAttribute('data-rashi');
      if (r && LAGNA_ORDER.indexOf(r.trim()) !== -1) return r.trim();
      var el = lagnaBox.querySelector('.lagna-name, .rashi-title-text');
      if (el) {{
        var t = el.textContent.trim().split(' ')[0];
        if (LAGNA_ORDER.indexOf(t) !== -1) return t;
      }}
    }}
    var h1 = document.querySelector('[data-house-no="1"]');
    if (h1) {{
      var r1 = h1.getAttribute('data-rashi');
      if (r1 && LAGNA_ORDER.indexOf(r1.trim()) !== -1) return r1.trim();
      var el1 = h1.querySelector('.lagna-name, .rashi-title-text');
      if (el1) {{
        var t1 = el1.textContent.trim().split(' ')[0];
        if (LAGNA_ORDER.indexOf(t1) !== -1) return t1;
      }}
    }}
    return "వృశ్చికం";
  }}

  // Calculate Bhava Lord placement rule based on 12 భావ ఫలాలు.pdf
  function getBhavaLordRuleItem(pName, placedHouseNum, chartLagna) {{
    if (!placedHouseNum || placedHouseNum < 1 || placedHouseNum > 12) return null;
    var normP = normalizePlanetName(pName);
    if (!normP) return null;
    var ownRasi = OWN_HOUSE_RULES[normP];
    if (!ownRasi) return null;

    var lagnaIdx = LAGNA_ORDER.indexOf(chartLagna);
    if (lagnaIdx === -1) lagnaIdx = 7; // default Vrischika
    var ownRasiIdx = LAGNA_ORDER.indexOf(ownRasi);
    var lordHouseNum = ((ownRasiIdx - lagnaIdx + 12) % 12) + 1;

    var isNativeGuru = (GURU_PARTY_LAGNAS.indexOf(chartLagna) !== -1);
    var isPlanetGuru = (GURU_PARTY_PLANETS.indexOf(normP) !== -1);
    var isFriend = (isNativeGuru === isPlanetGuru);

    var pHouseStr = String(placedHouseNum);
    var lHouseStr = String(lordHouseNum);

    var houseRules = BHAVA_LORD_RULES[pHouseStr];
    if (!houseRules) return null;
    var ruleEntry = houseRules[lHouseStr];
    if (!ruleEntry) return null;

    var ruleText = isFriend ? (ruleEntry.shubha || ruleEntry.paapa) : (ruleEntry.paapa || ruleEntry.shubha);
    if (!ruleText) return null;

    var displayName = PLANET_STANDARD_DISPLAY[normP] || normP;

    return {{
      lordHouseNum: lordHouseNum,
      planetName: displayName,
      placedHouseNum: placedHouseNum,
      isFriend: isFriend,
      ruleText: ruleText.trim()
    }};
  }}

  // Collect all distinct occupant planets in a box
  function getBoxOccupantPlanets(box, hoveredPlanetKey) {{
    var planets = [];
    var seen = {{}};

    var normHovered = normalizePlanetName(hoveredPlanetKey);
    if (normHovered && OWN_HOUSE_RULES[normHovered]) {{
      var stdHovered = PLANET_STANDARD_DISPLAY[normHovered] || normHovered;
      planets.push(stdHovered);
      seen[stdHovered] = true;
    }}

    if (box) {{
      // 1. Query child elements (pills, spans, aspect hands, etc.)
      var pills = box.querySelectorAll('.occupant-pill, .planet-name-pill, .aspect-hand, .planet-line-item, span.pos, span.neg, .lagna-text, b.full-name, [data-planet]');
      pills.forEach(function(pill) {{
        var rawText = pill.getAttribute('data-planet') || pill.textContent || '';
        for (var pKey in OWN_HOUSE_RULES) {{
          if (rawText.indexOf(pKey) !== -1) {{
            var norm = normalizePlanetName(pKey);
            if (norm && OWN_HOUSE_RULES[norm]) {{
              var std = PLANET_STANDARD_DISPLAY[norm] || norm;
              if (!seen[std]) {{
                planets.push(std);
                seen[std] = true;
              }}
            }}
            break;
          }}
        }}
      }});

      // 2. Query text lines inside box (for lines separated by <br>)
      var textLines = (box.innerText || box.textContent || '').split(/[\\n\\r]+/);
      textLines.forEach(function(line) {{
        if (line.indexOf('స్థానము') !== -1 || line.indexOf('పుణ్యం') !== -1 || line.indexOf('పాపం') !== -1) return;
        for (var pKey in OWN_HOUSE_RULES) {{
          if (line.indexOf(pKey) !== -1) {{
            var norm = normalizePlanetName(pKey);
            if (norm && OWN_HOUSE_RULES[norm]) {{
              var std = PLANET_STANDARD_DISPLAY[norm] || norm;
              if (!seen[std]) {{
                planets.push(std);
                seen[std] = true;
              }}
            }}
            break;
          }}
        }}
      }});
    }}

    return planets;
  }}

  // 1. Show Planet Graha Karakatwalu (ఆ గ్రహం ఆధీనంలో ఉన్నవి) & ఫలితాలు
  // Called ONLY when the mouse moves on a planet
  window.showGrahaKarakatwalu = function(planetKey, targetEl, evt, rashiContext) {{
    if (!window.isVivaranaEnabled()) return;

    if (hideTimeout) clearTimeout(hideTimeout);
    var pKey = normalizePlanetName(planetKey);
    if (!pKey || !PLANETS_DATA[pKey]) return;
    var p = PLANETS_DATA[pKey];
    createPopover();

    var currentHouse = rashiContext || '';
    var placedHouseNum = 0;
    var rashiName = '';
    var box = targetEl ? targetEl.closest('.box, .nak-box') : null;

    if (box) {{
      placedHouseNum = parseInt(box.getAttribute('data-house-no') || '0', 10);
      if (!placedHouseNum) {{
        var hnoEl = box.querySelector('.house-no, .house-badge');
        if (hnoEl) placedHouseNum = parseInt(hnoEl.textContent.trim(), 10) || 0;
      }}
      rashiName = box.getAttribute('data-rashi') || '';
      if (!rashiName) {{
        var rashiEl = box.querySelector('.lagna-name, .rashi-title-text');
        if (rashiEl) rashiName = rashiEl.textContent.trim().split(' ')[0];
      }}
    }}

    var chartLagna = getChartLagna(targetEl);
    if (!placedHouseNum && rashiName) {{
      var lagnaIdx = LAGNA_ORDER.indexOf(chartLagna);
      var rashiIdx = LAGNA_ORDER.indexOf(rashiName);
      if (lagnaIdx !== -1 && rashiIdx !== -1) {{
        placedHouseNum = ((rashiIdx - lagnaIdx + 12) % 12) + 1;
      }}
    }}

    if (!currentHouse && (rashiName || placedHouseNum)) {{
      currentHouse = (rashiName ? rashiName + ' రాశి' : '') + (placedHouseNum ? ' (' + placedHouseNum + 'వ స్థానము)' : '');
    }}

    // Compute ಫಲితాలు (Bhava Lord rules) for occupants of this house
    var boxOccupants = getBoxOccupantPlanets(box, pKey);
    var ruleItems = [];
    var seenLords = {{}};

    boxOccupants.forEach(function(occPlanet) {{
      var item = getBhavaLordRuleItem(occPlanet, placedHouseNum, chartLagna);
      if (item && !seenLords[item.lordHouseNum + '_' + item.planetName]) {{
        seenLords[item.lordHouseNum + '_' + item.planetName] = true;
        ruleItems.push(item);
      }}
    }});

    if (ruleItems.length === 0 && placedHouseNum) {{
      var item = getBhavaLordRuleItem(pKey, placedHouseNum, chartLagna);
      if (item) ruleItems.push(item);
    }}

    // Sort by lordHouseNum in ascending order (1, 4, 5, 6, 12...)
    ruleItems.sort(function(a, b) {{
      return a.lordHouseNum - b.lordHouseNum;
    }});

    var normHoveredStd = PLANET_STANDARD_DISPLAY[pKey] || pKey;
    var bhavaLordRulesHtml = '';
    if (ruleItems.length > 0) {{
      bhavaLordRulesHtml = ruleItems.map(function(item) {{
        // Color rule requested by user:
        // If this planet is in red colour: ALL the text is in RED colour result.
        // If it is green: ALL its related result text is in GREEN colour.
        var isCurrentHovered = (item.planetName === normHoveredStd || pKey.indexOf(item.planetName) !== -1 || item.planetName.indexOf(pKey) !== -1);
        var itemColor = item.isFriend ? '#4ade80' : '#f87171';
        var itemBorder = item.isFriend ? '#22c55e' : '#ef4444';
        var itemBg = item.isFriend ? 'rgba(34, 197, 94, 0.12)' : 'rgba(239, 68, 68, 0.12)';
        var extraStyle = isCurrentHovered
          ? 'box-shadow: 0 0 10px ' + (item.isFriend ? 'rgba(34,197,94,0.3)' : 'rgba(239,68,68,0.3)') + ';'
          : '';

        return '<div style="margin-bottom: 11px; line-height: 1.75; font-size: 12.5px; background: ' + itemBg + '; border-left: 3.5px solid ' + itemBorder + '; padding: 8px 11px; border-radius: 6px; border-top: 1px solid rgba(255,255,255,0.05); border-right: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05); ' + extraStyle + '">' +
          '<strong style="color: ' + itemColor + '; font-weight: 800; display: inline;">' + item.lordHouseNum + 'వ స్థానాధిపతి (' + item.planetName + ') ' + item.placedHouseNum + 'వ స్థానములో ఉన్నందున:</strong> ' +
          '<span style="color: ' + itemColor + '; display: inline;">' + item.ruleText + '</span>' +
        '</div>';
      }}).join('');
    }}

    var headerBg = (p.party && p.party.indexOf('గురు') !== -1)
      ? 'linear-gradient(135deg, #065f46 0%, #064e3b 100%)'
      : (p.party && p.party.indexOf('శని') !== -1)
      ? 'linear-gradient(135deg, #881337 0%, #4c0519 100%)'
      : 'linear-gradient(135deg, #312e81 0%, #1e1b4b 100%)';

    var html = [
      '<div style="background: ' + headerBg + '; padding: 10px 14px; border-bottom: 2px solid rgba(245,158,11,0.4); display: flex; align-items: center; justify-content: space-between;">',
        '<div>',
          '<div style="font-size: 15px; font-weight: 800; color: #ffd700; text-shadow: 0 1px 3px rgba(0,0,0,0.8); display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">',
            '<span>🪐 ' + p.display_name + '</span>',
            '<span style="background: ' + (p.party_color || '#10b981') + '; color: #ffffff; font-size: 11px; padding: 2px 8px; border-radius: 12px; font-weight: 700;">' + p.party + '</span>',
          '</div>',
          '<div style="font-size: 11.5px; color: #e2e8f0; margin-top: 3px;">',
            'దిశ: <b>' + p.direction + '</b> | రత్నం: <b>' + p.gem + '</b> | జాతి: <b>' + p.caste + '</b> (' + p.color_desc + ')',
          '</div>',
        '</div>',
        '<button type="button" onclick="document.getElementById(\\'astro-interactive-popover\\').style.display=\\'none\\'" style="background: transparent; border: none; color: #cbd5e1; font-size: 20px; cursor: pointer; padding: 0 4px; line-height: 1; font-weight: bold;">&times;</button>',
      '</div>',
      '<div style="padding: 12px 14px; max-height: 440px; overflow-y: auto; box-sizing: border-box; background: #0f172a;">',
        (currentHouse ? '<div style="background: rgba(245,158,11,0.12); border-left: 3px solid #f59e0b; padding: 5px 9px; margin-bottom: 9px; font-size: 12px; font-weight: 700; color: #fbbf24;">📍 ప్రస్తుత స్థానము: ' + currentHouse + '</div>' : ''),
        '<div style="font-size: 12.5px; font-weight: 800; color: #fbbf24; margin-bottom: 6px; display: flex; align-items: center; gap: 5px;">',
          '<span>📖</span> ఆ గ్రహం ఆధీనంలో ఉన్నవి (గ్రహ కారకత్వాలు):',
        '</div>',
        '<div style="font-size: 12px; line-height: 1.6; color: #f1f5f9; background: rgba(30,41,59,0.7); padding: 9px 11px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08); text-align: justify; margin-bottom: 12px;">',
          (p.governed_items || p.karakatwalu || ''),
        '</div>',
        (bhavaLordRulesHtml ? [
          '<div style="font-size: 12.5px; font-weight: 800; color: #38bdf8; margin-bottom: 6px; display: flex; align-items: center; gap: 5px;">',
            '<span>📜</span> ఫలితాలు:',
          '</div>',
          '<div style="font-size: 12px; line-height: 1.7; color: #cbd5e1; background: rgba(15,23,42,0.85); padding: 11px 13px; border-radius: 8px; border: 1px solid rgba(56,189,248,0.25); text-align: justify;">',
            bhavaLordRulesHtml,
          '</div>'
        ].join('') : ''),
      '</div>'
    ].join('');

    popover.innerHTML = html;
    currentTarget = targetEl;
    positionPopover(targetEl, evt ? evt.clientX : 0, evt ? evt.clientY : 0);
  }};

  // 2. Show House Information from Jyothishya Shaasthramu
  // Called when mouse moves on a house box (NO ఫలితాలు here as per user request)
  window.showHouseJyothishyaInfo = function(houseNo, targetEl, evt, rashiName) {{
    if (!window.isVivaranaEnabled()) return;

    if (hideTimeout) clearTimeout(hideTimeout);
    var hKey = String(houseNo).trim();
    if (!hKey || !HOUSES_DATA[hKey]) return;
    var h = HOUSES_DATA[hKey];
    createPopover();

    var occupantsList = [];
    var rashi = rashiName || '';
    var box = targetEl ? targetEl.closest('.box, .nak-box') : null;

    if (box) {{
      if (!rashi) {{
        var rashiEl = box.querySelector('.lagna-name, .rashi-title-text');
        if (rashiEl) rashi = rashiEl.textContent.trim().split(' ')[0];
      }}
      box.querySelectorAll('.occupant-pill, .planet-line-item, .lagna-text, span.pos, span.neg, b.full-name').forEach(function(pill) {{
        var t = pill.textContent.replace(/[🚩👉*⏱️]+/g, '').trim();
        if (t && occupantsList.indexOf(t) === -1 && t.length > 1) occupantsList.push(t);
      }});
    }}

    var occupantsHtml = occupantsList.length > 0
      ? '<span style="color: #38bdf8; font-weight: 700;">' + occupantsList.join(', ') + '</span>'
      : '<span style="color: #94a3b8; font-style: italic;">ఏ గ్రహాలూ లేవు (ఖాళీ స్థానము)</span>';

    var html = [
      '<div style="background: linear-gradient(135deg, #7c2d12 0%, #451a03 100%); padding: 10px 14px; border-bottom: 2px solid rgba(251,191,36,0.4); display: flex; align-items: center; justify-content: space-between;">',
        '<div>',
          '<div style="font-size: 15px; font-weight: 800; color: #ffd700; text-shadow: 0 1px 3px rgba(0,0,0,0.8); display: flex; align-items: center; gap: 8px;">',
            '<span>🏛️ ' + h.name + '</span>',
            '<span style="background: rgba(251,191,36,0.25); border: 1px solid #fbbf24; color: #fbbf24; font-size: 11px; padding: 2px 8px; border-radius: 12px; font-weight: 800;">' + h.house_no + 'వ భావం</span>',
          '</div>',
          '<div style="font-size: 11.5px; color: #fde68a; margin-top: 3px;">',
            (rashi ? 'రాశి: <b>' + rashi + '</b> | ' : '') + 'కర్మ విధానము: <b>' + h.karma_type + '</b>',
          '</div>',
        '</div>',
        '<button type="button" onclick="document.getElementById(\\'astro-interactive-popover\\').style.display=\\'none\\'" style="background: transparent; border: none; color: #cbd5e1; font-size: 20px; cursor: pointer; padding: 0 4px; line-height: 1; font-weight: bold;">&times;</button>',
      '</div>',
      '<div style="padding: 12px 14px; max-height: 440px; overflow-y: auto; box-sizing: border-box; background: #0f172a;">',
        '<div style="background: rgba(56,189,248,0.1); border-left: 3px solid #0284c7; padding: 5px 9px; margin-bottom: 8px; font-size: 12px; border-radius: 0 6px 6px 0;">',
          '<b style="color: #38bdf8;">ఈ స్థానంలో ఉన్నవి:</b> ' + occupantsHtml,
        '</div>',
        '<div style="background: rgba(245,158,11,0.1); border-left: 3px solid #f59e0b; padding: 5px 9px; margin-bottom: 9px; font-size: 12px; border-radius: 0 6px 6px 0;">',
          '<b style="color: #fbbf24;">స్థాన కారకత్వాలు:</b> <span style="color: #f1f5f9;">' + h.karakatwalu + '</span>',
        '</div>',
        '<div style="font-size: 12.5px; font-weight: 800; color: #ffd700; margin-bottom: 5px; display: flex; align-items: center; gap: 5px;">',
          '<span>📖</span> జ్యోతిష్య శాస్త్రము (గ్రంథ వివరణ):',
        '</div>',
        '<div style="font-size: 11.5px; line-height: 1.65; color: #f8fafc; background: rgba(30,41,59,0.7); padding: 9px 11px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08); text-align: justify;">',
          h.book_excerpt,
        '</div>',
      '</div>'
    ].join('');

    popover.innerHTML = html;
    currentTarget = targetEl;
    positionPopover(targetEl, evt ? evt.clientX : 0, evt ? evt.clientY : 0);
  }};

  // Auto-bind Event Listeners on Page Load and AJAX updates
  function bindAstroHoverListeners() {{
    injectVivaranaStyles();
    window.updateVivaranaButtonUI();
    createPopover();

    var planetSelectors = [
      '.occupant-pill',
      '.planet-name-pill',
      '.lagna-occupant',
      '.aspect-hand',
      '.planet-line-item',
      '.lagna-text',
      'span.pos',
      'span.neg',
      'b.full-name',
      '[data-planet]'
    ].join(',');

    document.querySelectorAll(planetSelectors).forEach(function(el) {{
      if (el.getAttribute('data-astro-planet-bound')) return;
      el.setAttribute('data-astro-planet-bound', 'true');
      el.style.cursor = 'help';

      el.addEventListener('mouseenter', function(e) {{
        e.stopPropagation();
        var pName = el.getAttribute('data-planet') || el.textContent;
        var rashiCtx = el.getAttribute('data-rashi-context') || '';
        window.showGrahaKarakatwalu(pName, el, e, rashiCtx);
      }});

      el.addEventListener('mouseleave', function(e) {{
        scheduleHide(200);
      }});

      el.addEventListener('click', function(e) {{
        e.stopPropagation();
        var pName = el.getAttribute('data-planet') || el.textContent;
        var rashiCtx = el.getAttribute('data-rashi-context') || '';
        window.showGrahaKarakatwalu(pName, el, e, rashiCtx);
      }});
    }});

    var boxSelectors = [
      '.box',
      '.nak-box',
      '.house-no',
      '.house-badge',
      '.nak-box-header',
      '[data-house-no]'
    ].join(',');

    document.querySelectorAll(boxSelectors).forEach(function(el) {{
      if (el.getAttribute('data-astro-box-bound')) return;
      el.setAttribute('data-astro-box-bound', 'true');

      var isBadgeOrHeader = el.classList.contains('house-no') || el.classList.contains('house-badge') || el.classList.contains('nak-box-header');
      if (isBadgeOrHeader) {{
        el.style.cursor = 'help';
        el.title = 'ఈ స్థానము వివరాలు & ఫలితాలు చూడండి';
      }}

      el.addEventListener('mouseenter', function(e) {{
        if (e.target.closest(planetSelectors)) return;
        var boxEl = el.closest('.box, .nak-box') || el;
        var hno = boxEl.getAttribute('data-house-no');
        var rashi = boxEl.getAttribute('data-rashi');
        if (!hno) {{
          var hnoEl = boxEl.querySelector('.house-no, .house-badge');
          if (hnoEl) hno = hnoEl.textContent.trim();
        }}
        if (!rashi) {{
          var rashiEl = boxEl.querySelector('.lagna-name, .rashi-title-text');
          if (rashiEl) rashi = rashiEl.textContent.trim().split(' ')[0];
        }}
        if (hno) {{
          window.showHouseJyothishyaInfo(hno, isBadgeOrHeader ? el : boxEl, e, rashi);
        }}
      }});

      el.addEventListener('mouseleave', function(e) {{
        scheduleHide(200);
      }});

      el.addEventListener('click', function(e) {{
        if (e.target.closest(planetSelectors)) return;
        var boxEl = el.closest('.box, .nak-box') || el;
        var hno = boxEl.getAttribute('data-house-no');
        var rashi = boxEl.getAttribute('data-rashi');
        if (!hno) {{
          var hnoEl = boxEl.querySelector('.house-no, .house-badge');
          if (hnoEl) hno = hnoEl.textContent.trim();
        }}
        if (!rashi) {{
          var rashiEl = boxEl.querySelector('.lagna-name, .rashi-title-text');
          if (rashiEl) rashi = rashiEl.textContent.trim().split(' ')[0];
        }}
        if (hno) {{
          window.showHouseJyothishyaInfo(hno, el, e, rashi);
        }}
      }});
    }});
  }}

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', bindAstroHoverListeners);
  }} else {{
    bindAstroHoverListeners();
  }}

  window.initAstroInteractivePopovers = bindAstroHoverListeners;

}})();
'''

with open('static/js/astro_interactive_popover.js', 'w', encoding='utf-8') as f:
    f.write(js_template)

print("Successfully written updated static/js/astro_interactive_popover.js! Total bytes:", len(js_template.encode('utf-8')))

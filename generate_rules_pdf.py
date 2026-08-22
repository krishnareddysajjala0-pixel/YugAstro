# -*- coding: utf-8 -*-
"""
Generate Master Rules PDF file using Python ReportLab.
Aggregates all 144 Bhava Lord Placement Rules, 12 House Meanings, 12 Planet Constants,
Yoga Rules, and 40 Topic Mappings into a downloadable PDF document.
"""

import os
import sys
import json
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Import Rules Exporter
from results_engine.rules_exporter import RulesExporter

def build_pdf(output_path="static/YugAstro_All_Rules_Master_Handbook.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    dataset = RulesExporter.get_all_rules_dataset()

    # Try registering Nirmala / Segoe / Arial TrueType font for Unicode/Telugu support
    font_name = "Helvetica"
    font_path_nirmala = "C:/Windows/Fonts/Nirmala.ttc"
    font_path_segoe = "C:/Windows/Fonts/segoeui.ttf"
    font_path_arial = "C:/Windows/Fonts/arial.ttf"

    if os.path.exists(font_path_segoe):
        try:
            pdfmetrics.registerFont(TTFont('SegoeUI', font_path_segoe))
            font_name = 'SegoeUI'
        except Exception as e:
            print("Font register notice:", e)

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName=font_name,
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#1e3a8a'),
        alignment=1, # Center
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName=font_name,
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#475569'),
        alignment=1,
        spaceAfter=16
    )

    h1_style = ParagraphStyle(
        'ChapterH1',
        parent=styles['Heading2'],
        fontName=font_name,
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#b45309'),
        spaceBefore=14,
        spaceAfter=8
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontName=font_name,
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#0f766e'),
        spaceBefore=10,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName=font_name,
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=4
    )

    shubha_style = ParagraphStyle(
        'ShubhaStyle',
        parent=body_style,
        textColor=colors.HexColor('#047857')
    )

    paapa_style = ParagraphStyle(
        'PaapaStyle',
        parent=body_style,
        textColor=colors.HexColor('#b91c1c')
    )

    story = []

    # Title & Subtitle
    story.append(Paragraph(dataset["title"], title_style))
    story.append(Paragraph(dataset["subtitle"], subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#f59e0b'), spaceAfter=14))

    # Overview Table
    summary_data = [
        [Paragraph("<b>భావాలయ్యాధిపతి నియమాలు:</b> 144 నియమాలు", body_style), Paragraph("<b>12 భావార్థాలు:</b> 12 భావాలు", body_style)],
        [Paragraph("<b>12 గ్రహ కారకత్వాలు:</b> 12 గ్రహాలు", body_style), Paragraph("<b>రంగాల మ్యాపింగ్:</b> 40 రంగాలు", body_style)]
    ]
    sum_table = Table(summary_data, colWidths=[260, 260])
    sum_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fef3c7')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#f59e0b')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#fde68a')),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(sum_table)
    story.append(Spacer(1, 14))

    # Chapter 1: 12 Planets
    story.append(Paragraph("అధ్యాయము 1: 12 గ్రహముల త్రైత విధానము & కారకత్వములు", h1_style))
    p_rows = [[Paragraph("<b>గ్రహము</b>", body_style), Paragraph("<b>వర్గం</b>", body_style), Paragraph("<b>స్వక్షేత్రం</b>", body_style), Paragraph("<b>కారకత్వము</b>", body_style)]]
    for p in dataset["planets"]:
        p_rows.append([
            Paragraph(p["name"], body_style),
            Paragraph(p["party"], body_style),
            Paragraph(p["ruler_sign"] or "విశేషం", body_style),
            Paragraph(p["karakatwa"], body_style)
        ])
    p_table = Table(p_rows, colWidths=[70, 70, 70, 310])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 14))

    # Chapter 2: 12 House Meanings
    story.append(Paragraph("అధ్యాయము 2: 12 భావముల ఫలితాలు & విశేష అర్థాలు", h1_style))
    for h in dataset["house_meanings"]:
        story.append(Paragraph(f"<b>{h['title']}</b>", h2_style))
        story.append(Paragraph(f"<b>భావ కారకత్వం:</b> {h['meaning']}", body_style))
        if h['shubha']:
            story.append(Paragraph(f"<b>🟢 శుభ నియమం:</b> {h['shubha']}", shubha_style))
        if h['paapa']:
            story.append(Paragraph(f"<b>🔴 హెచ్చరిక నియమం:</b> {h['paapa']}", paapa_style))
        story.append(Spacer(1, 4))

    story.append(PageBreak())

    # Chapter 3: 12x12 Placement Matrix (144 Rules)
    story.append(Paragraph("అధ్యాయము 3: 12×12 భావాధిపతుల స్థాన ఫలముల మాతృక (144 సంపూర్ణ నియమాలు)", h1_style))
    for hm in dataset["lord_matrix"]:
        story.append(Paragraph(f"<b>{hm['house_title']}</b>", h2_style))
        for p in hm["placements"]:
            s_txt = f" | <b>శుభం:</b> {p['shubha']}" if p['shubha'] else ""
            p_txt = f" | <b>హెచ్చరిక:</b> {p['paapa']}" if p['paapa'] else ""
            story.append(Paragraph(f"• <b>[{p['rule_id']}] {p['title']}</b>{s_txt}{p_txt}", body_style))
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # Chapter 4: Yogas
    story.append(Paragraph("అధ్యాయము 4: రాశి చక్ర యోగముల నియమావళి", h1_style))
    for y in dataset["yogas"]:
        story.append(Paragraph(f"<b>{y.get('name_te')}</b> (మూలం: {y.get('source')}, బలం: {y.get('strength')})", h2_style))
        story.append(Paragraph(f"{y.get('result_te')}", body_style))

    story.append(Spacer(1, 14))

    # Chapter 5: 40 Topics Mapping
    story.append(Paragraph("అధ్యాయము 5: 40 రంగాలు & నియమ అనుసంధాన ప్రక్రియ", h1_style))
    t_rows = [[Paragraph("<b>రంగము</b>", body_style), Paragraph("<b>అనుమతించబడిన భావాలు</b>", body_style), Paragraph("<b>కారకత్వ గ్రహాలు</b>", body_style)]]
    for t in dataset["topics"]:
        t_rows.append([
            Paragraph(t["name"], body_style),
            Paragraph(t["allowed_houses"], body_style),
            Paragraph(t["allowed_planets"] or "విశేష గ్రహాలు", body_style)
        ])
    t_table = Table(t_rows, colWidths=[120, 150, 250])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_table)

    doc.build(story)
    print(f"Master Rules PDF built successfully at: {output_path}")
    return output_path

if __name__ == "__main__":
    build_pdf()

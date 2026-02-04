from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import random

MESSAGES = [
    "You've got this.",
    "One step at a time.",
    "Breathe. Relax your shoulders.",
    "Progress > perfection.",
    "Do your best. Flush the rest.",
    "You are allowed to take breaks.",
    "Future you will thank you.",
    "Small wins count.",
]

def make_cards_pdf(path="toilet_encouragement_cards.pdf", cols=2, rows=4, margin=0.5*inch):
    w, h = letter
    c = canvas.Canvas(path, pagesize=letter)

    card_w = (w - 2*margin) / cols
    card_h = (h - 2*margin) / rows

    c.setTitle("Toilet Encouragement Cards")

    for r in range(rows):
        for col in range(cols):
            x = margin + col * card_w
            y = h - margin - (r+1) * card_h

            # border
            c.rect(x+6, y+6, card_w-12, card_h-12)

            # message
            msg = random.choice(MESSAGES)
            c.setFont("Helvetica-Bold", 18)
            c.drawCentredString(x + card_w/2, y + card_h/2 + 8, msg)

            c.setFont("Helvetica", 10)
            c.drawCentredString(x + card_w/2, y + 18, "🚽 tiny pep talk")

    c.showPage()
    c.save()
    print(f"Saved: {path}")

if __name__ == "__main__":
    make_cards_pdf()
radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)

import streamlit as st

st.set_page_config(page_title="AI Buddy Chatbot", layout="centered")
st.title("🤖 AI Buddy - Your Shop Assistant")
st.write("Ask me anything about your shop, products, or services!")

shop_info = {
    "pen": "Yes, we have Cello, Reynolds, and Parker pens starting from ₹5.",
    "notebook": "We have Classmate and Navneet notebooks in A4 and long sizes.",
    "medicine": "We sell common OTC medicines like Paracetamol, ORS, and cough syrup.",
    "location": "We are located at Bibirhat Bazar, near the main road.",
    "timing": "Shop open: 9 AM to 9 PM (every day).",
    "payment": "We accept Cash, UPI, PhonePe, and Paytm."
    "pen": "Yes, we have Cello, Reynolds, and Parker pens starting from ₹5.",
    "notebook": "We have Classmate and Navneet notebooks in A4 and long sizes.",
    "medicine": "We sell common OTC medicines like Paracetamol, ORS, and cough syrup.",
    "location": "We are located at Bibirhat Bazar, near the main road.",
    "timing": "Shop open: 9 AM to 9 PM (every day).",
    "payment": "We accept Cash, UPI, PhonePe, and Paytm.",
    "calculator": "Yes, we sell Casio and Orpat calculators, starting at ₹250.",
    "xerox": "Yes, we provide black & white and color Xerox facilities.",
    "print": "We offer printout services in A4 and legal size formats.",
    "stationery": "You’ll find pens, pencils, erasers, rulers, staplers, and more.",
    "admission form": "Yes, we print and fill up online admission forms.",
    "smartphone": "Sorry, we don't sell smartphones currently.",
    "delivery": "We offer free local delivery on orders above ₹200.",
    "return policy": "Items can be returned within 3 days with proper receipt.",
    "online payment": "Yes, UPI (GPay, PhonePe, Paytm) is accepted.",
    "upi": "You can pay using UPI QR code at the counter."
}

}

def ai_buddy_response(user_input):
    user_input = user_input.lower()
    for keyword in shop_info:
        if keyword in user_input:
            return shop_info[keyword]
    return "Sorry, I couldn't understand. Please ask something about products or shop info."

user_input = st.text_input("Type your question here:", "Do you have notebook?")

if st.button("Ask AI Buddy"):
    response = ai_buddy_response(user_input)
    st.success(response)

st.markdown("---")
st.markdown("Made by Imran's AI Buddy ❤️ For Bibirhat Shop Support")

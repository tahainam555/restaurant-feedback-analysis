import streamlit as st
import json

# Load the JSON data
with open("processed_reviews.json", "r", encoding="utf-8") as file:
    reviews = json.load(file)

# Add a background image
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1551524164-687a55dd1126?crop=entropy&cs=tinysrgb&fit=max&ixid=MXwyMDg0OXwwfDF8c2VhcmNofDJ8fGZvb2R8ZW58MHx8fHwxNjY4NjU1NzU5&ixlib=rb-1.2.1&q=80&w=1080");    background-size: cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
    background-position: center;
    color: white;
}

h1 {
    color: white;
    text-align: center;
    padding: 20px;
    font-size: 3em;
    text-shadow: 2px 2px 5px rgba(0,0,0,0.7);
}

.review-card {
    background-color: rgba(0, 0, 0, 0.7);
    border-radius: 10px;
    padding: 20px;
    margin: 20px 0;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s;
}

.review-card:hover {
    transform: translateY(-5px);
}

.review-card .rating {
    font-size: 1.5em;
    color: #ffcc00;
}

.review-card .review-title {
    font-size: 1.2em;
    font-weight: bold;
}

.review-card .review-body {
    margin-top: 10px;
}

.review-card .food-quality, .review-card .staff-service {
    margin-top: 10px;
    font-style: italic;
    font-size: 1.1em;
}

footer {
    text-align: center;
    margin-top: 50px;
    color: #ccc;
    font-size: 0.8em;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title of the app
st.title("Restaurant Reviews Dashboard")

# Display all reviews
for review in reviews:
    if review['food_quality'] ==  "" and review['staff_service'] == "":
        continue
    if review['food_quality'] ==  "No comments on food quality." and review['staff_service'] == "No comments on staff service.":
        continue
    st.markdown("<hr>", unsafe_allow_html=True)  # Add a horizontal separator for each review
    # Create a review card
    with st.container():
        review_card = f"""
        <div class="review-card">
            <div class="review-title">
                Customer: {review['name']} (Dined: {review['dining_time']})
            </div>
            <div class="rating">
                **Rating:** {review['rating']} ⭐
            </div>
            <div class="review-body">
                <div class="food-quality">
                    {f"<span style='color: lightgreen;'>**Food Quality:** {review['food_quality']}</span>" if review.get('food_quality') else "<span style='color: lightgreen;'>**Food Quality:** Not Available</span>"}
                </div>
                <div class="staff-service">
                    {f"<span style='color: lightblue;'>**Staff/Service:** {review['staff_service']}</span>" if review.get('staff_service') else "<span style='color: lightblue;'>**Staff/Service:** Not Available</span>"}
                </div>
            </div>
        </div>
        """
        st.markdown(review_card, unsafe_allow_html=True)

# Footer
st.markdown("<footer>End of reviews.</footer>", unsafe_allow_html=True)

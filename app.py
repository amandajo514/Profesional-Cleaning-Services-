import streamlit as st

# Set page title and icon
st.set_page_config(page_title = "CoveClean Innovations", page_icon = "🧹")

#Sidebar navigation
page = st.sidebar.selectbox("Select a Page", ["🧹 About Us", "🧽 Home Cleaning Pricing", "🧼 Corporate Office Cleaning Pricing", "🧺 What Makes Us Different?", "🧻 Contact Us"])

# setting color theme
custom_theme = f"""
    <style>
        :root {{
            --primaryColor: #9C8777;
            --backgroundColor: #FFE2D3;
            --secondaryBackgroundColor: #E2C3B2;
            --textColor: #543022;
            --font: sans-serif;
        }}
    </style>
"""

st.markdown(custom_theme, unsafe_allow_html=True)

# Build homepage
if page == "🧹 About Us":
    st.title("🧹 About Us:")
    st.subheader("CoveClean Innovations:")
    
    st.write("Transforming spaces one cove at a time!")
    
    # Define the file path to your logo image
    logo_path = "coveclean_innovations_logo.png"

    # Display the image
    st.image(logo_path, 
            use_column_width=True,
            output_format="auto",
            width=0.5) 
    
    st.write("Please use the toggle bar on the left hand side of the page to navigate between our services, pricing, differentiators, and contact information.")

#build home cleaning services & pricing page
if page == "🧽 Home Cleaning Pricing":
    st.title("Professional Home Cleaning")
    st.title("🧽 Services & Pricing")

    st.markdown('<div class="center">', unsafe_allow_html=True)
    
    # Basic Service Column
    st.markdown('<div class="service-column">', unsafe_allow_html=True)
    st.write("**Basic**")
    st.markdown('<div class="price">$300</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">The basic price for cleaning services for a standard size house includes a three-hour job covering up to seven rooms, encompassing living rooms, dining rooms, bathrooms, bedrooms, and similar spaces.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Medium Service Column
    st.markdown('<div class="service-column">', unsafe_allow_html=True)
    st.write("**Medium**")
    st.markdown('<div class="price">$350</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">The medium price tier covers cleaning services for a total of up to seven rooms, up to 5 hours of work, accommodating various living spaces such as living rooms, dining rooms, bathrooms, bedrooms, and more.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Large Service Column
    st.markdown('<div class="service-column">', unsafe_allow_html=True)
    st.write("**Large**")
    st.markdown('<div class="price">$400+ (Custom Quote) </div>', unsafe_allow_html=True)
    st.markdown('<div class="description">The large price tier encompasses cleaning services for properties exceeding a total of seven rooms, offering comprehensive cleaning for larger living spaces. Pricing & job length subject to in home consultaiton.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


#build corporate office cleaning services & pricing page
    
if page == "🧼 Corporate Office Cleaning Pricing":
    st.title("Corporate Office Cleaning")
    st.title("🧼 Services & Pricing")

    st.markdown('<div class="center">', unsafe_allow_html=True)
    
    # Basic Service Column
    st.markdown('<div class="service-column">', unsafe_allow_html=True)
    st.write("**Basic**")
    st.markdown('<div class="price">$300</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">Suitable for small to medium-sized office spaces with standard cleaning requirements. This tier offers essential cleaning services for common areas, workspaces, and restrooms.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Medium Service Column
    st.markdown('<div class="service-column">', unsafe_allow_html=True)
    st.write("**Medium**")
    st.markdown('<div class="price">$400</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">Designed for medium to large-sized office environments with moderate cleaning needs. This tier includes comprehensive cleaning of all office areas, including dusting, vacuuming, mopping, sanitizing, and waste removal.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Large Service Column
    st.markdown('<div class="service-column">', unsafe_allow_html=True)
    st.write("**Large**")
    st.markdown('<div class="price">$600+ (Custom Quote) </div>', unsafe_allow_html=True)
    st.markdown('<div class="description">Tailored for large corporate offices or those requiring specialized cleaning services. This tier offers enhanced cleaning solutions such as deep cleaning, carpet shampooing, and additional amenities like restroom restocking. Pricing subject to in office consultation.</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    
# Build what makes us different page
if page == "🧺 What Makes Us Different?":
    st.title("🧺 What Makes Us Different")
    
    # Define bullet points
    bullet_points = {
        "Convenient Online Booking:": "Our user-friendly online booking platform allows clients to schedule cleaning services effortlessly. With just a few clicks, customers can select their preferred date, time, and services, making the booking process quick and convenient.",
        "Comprehensive Service Coverage:": "We cover a wide range of cleaning tasks, including dusting surfaces, vacuuming floors, mopping hard floors, disinfecting bathrooms, wiping down kitchen surfaces, and much more.",
        "Customized Solutions:": "Our services are tailored to meet the unique needs of each client. Whether it's a specific cleaning schedule, special requests, or preferences, we accommodate individual requirements.",
        "Attention to Detail:": "We pay meticulous attention to detail in every aspect of our cleaning process, ensuring that no corner is left untouched. We strive for thoroughness.",
        "Professional Staff:": "Our team consists of trained professionals who are experienced in delivering high- quality cleaning services. They are dedicated to providing exceptional results and exceeding client expectations.",
        "Commitment to Sanitation: ": "We prioritize sanitation and hygiene, especially in high-touch areas. By regularly sanitizing, we contribute to a healthier environment.",
        "Customer Convenience:": "We aim to make the cleaning experience hassle-free for our clients. From using cleaner-provided cleaning supplies to offering flexible scheduling options, we prioritize convenience and satisfaction."
    }
    
    # Display bullet points
    for bullet, description in bullet_points.items():
        st.markdown(f"**{bullet}:** {description}")
   
# Build contact us page
if page == "🧻 Contact Us":
    st.title("🧻 Contact Us")
    st.write("Contact Us!")
    st.write("Feel free to reach out to us via the following methods:")
    st.markdown("- Phone Number: :telephone_receiver: 518-860-5133")
    st.markdown("- Email: :email: amandajo514@gmail.com")
    st.markdown("- Booking Calendly Link: [Book a cleaning service](https://calendly.com/covecleaninnovations/cleaningservices?month=2024-03)")
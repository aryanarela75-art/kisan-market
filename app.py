import streamlit as st
import pandas as pd

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Kisan Market",
    page_icon="🌾",
    layout="wide"
)

# ---------------- SIDEBAR ----------------

st.sidebar.title("🌾 Kisan Market")
st.sidebar.write("Smart Market Linkage Platform")

page = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Home",
        "🌾 Farmer",
        "📊 Market Intelligence",
        "🤝 Buyer & Deals",
        "🚚 Logistics",
        "💰 Payments",
        "⚠️ Grievances",
        "🛠️ Admin Dashboard"
    ]
)

# ---------------- HOME ----------------

if page == "🏠 Home":

    st.title("🌾 KISAN MARKET")
    st.subheader("Smart Market Linkage & Price Discovery Platform")

    st.write(
        "Helping farmers discover better markets, connect with verified buyers, "
        "reduce transaction costs and improve price realisation."
    )

    st.divider()

    # Platform Statistics
    st.subheader("📊 Platform Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🌾 Crop Lots", "128")

    with col2:
        st.metric("🤝 Verified Buyers", "46")

    with col3:
        st.metric("📦 Active Deals", "32")

    with col4:
        st.metric("💰 Transactions", "₹12.8 Lakh")

    st.divider()

    # How the platform works
    st.subheader("🔄 From Farm to Buyer")

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    with c1:
        st.markdown("### 🌾")
        st.write("**Farm**")
        st.caption("Create crop lot")

    with c2:
        st.markdown("### 📊")
        st.write("**Market**")
        st.caption("Compare prices")

    with c3:
        st.markdown("### 🤝")
        st.write("**Buyer**")
        st.caption("Find verified buyers")

    with c4:
        st.markdown("### 💼")
        st.write("**Deal**")
        st.caption("Receive offers")

    with c5:
        st.markdown("### 🚚")
        st.write("**Logistics**")
        st.caption("Arrange transport")

    with c6:
        st.markdown("### 💰")
        st.write("**Payment**")
        st.caption("Track payment")

    st.divider()

    # Main Innovation
    st.subheader("⭐ Best Realisation Engine")

    st.info(
        "Kisan Market does not simply show the highest market price. "
        "It calculates the farmer's expected NET REALISATION after transport "
        "and other costs."
    )

    st.code(
        "NET REALISATION = SALE VALUE − TRANSPORT COST − OTHER COSTS",
        language="text"
    )

    st.success(
        "🎯 Goal: Help farmers choose the market or buyer that gives "
        "the best actual earning."
    )

    st.divider()

    # Key Features
    st.subheader("🚀 Key Features")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown("### 📈 Price Intelligence")
        st.write(
            "Compare market prices and identify price trends "
            "to support better selling decisions."
        )

    with f2:
        st.markdown("### 🤝 Verified Buyer Matching")
        st.write(
            "Connect farmers and FPOs with suitable verified buyers "
            "based on crop, quantity and quality."
        )

    with f3:
        st.markdown("### 🚚 Complete Transaction")
        st.write(
            "Manage deals, logistics, delivery, payments and "
            "grievances through one platform."
        )

    st.divider()

    st.success(
        "🌱 Better Information → Better Market → Better Negotiation → Better Farmer Income"
    )

# ---------------- FARMER ----------------

elif page == "🌾 Farmer":

    st.title("🌾 Farmer Dashboard")
    st.write("Create and manage your crop lots for better market opportunities.")

    st.divider()

    st.subheader("📦 Create New Crop Lot")

    col1, col2 = st.columns(2)

    with col1:
        crop = st.selectbox(
            "🌱 Select Crop",
            ["Potato", "Wheat", "Tomato", "Onion", "Rice"]
        )

        quantity = st.number_input(
            "⚖️ Quantity (kg)",
            min_value=1,
            value=500
        )

        location = st.text_input(
            "📍 Farm Location",
            placeholder="Example: Agra, Uttar Pradesh"
        )

    with col2:
        quality = st.selectbox(
            "⭐ Quality Grade",
            ["Grade A", "Grade B", "Grade C"]
        )

        expected_price = st.number_input(
            "💰 Minimum Expected Price (₹/kg)",
            min_value=1.0,
            value=20.0,
            step=0.5
        )

        harvest_date = st.date_input(
            "📅 Expected Harvest / Availability Date"
        )

    st.divider()

    st.subheader("📋 Lot Summary")

    summary1, summary2, summary3 = st.columns(3)

    with summary1:
        st.metric("Crop", crop)

    with summary2:
        st.metric("Quantity", f"{quantity} kg")

    with summary3:
        st.metric("Expected Price", f"₹{expected_price}/kg")

    st.divider()

    if st.button("🚀 CREATE CROP LOT", use_container_width=True):

        if location.strip() == "":
            st.error("⚠️ Please enter your farm location.")

        else:
            estimated_value = quantity * expected_price

            st.success("✅ Crop lot created successfully!")

            st.info(
                f"Your {quantity} kg {crop} lot has been registered. "
                f"Expected minimum value: ₹{estimated_value:,.2f}"
            )

            st.write("### 🔎 Next Recommended Actions")

            a1, a2, a3 = st.columns(3)

            with a1:
                st.write("📊 **Compare Markets**")
                st.caption("Find markets offering better net realisation.")

            with a2:
                st.write("🤝 **Find Buyers**")
                st.caption("Connect with verified buyers.")

            with a3:
                st.write("🚚 **Plan Logistics**")
                st.caption("Estimate transport and storage costs.")
# ---------------- MARKET INTELLIGENCE ----------------

elif page == "📊 Market Intelligence":

    st.title("📊 Market Intelligence")

    st.write(
        "Compare markets and find where the farmer can get the "
        "best NET REALISATION."
    )

    market_data = {
        "Market": [
            "Agra Mandi",
            "Delhi Azadpur",
            "Mathura Mandi",
            "Jaipur Mandi"
        ],
        "Market Price (₹/kg)": [
            18, 22, 20, 21
        ],
        "Transport (₹/kg)": [
            1.5, 4.0, 2.0, 3.5
        ],
        "Other Cost (₹/kg)": [
            0.5, 1.0, 0.5, 0.5
        ]
    }

    market_df = pd.DataFrame(market_data)

    market_df["Net Realisation (₹/kg)"] = (
        market_df["Market Price (₹/kg)"]
        - market_df["Transport (₹/kg)"]
        - market_df["Other Cost (₹/kg)"]
    )

    st.dataframe(
        market_df,
        use_container_width=True
    )

    best_market = market_df.loc[
        market_df["Net Realisation (₹/kg)"].idxmax()
    ]

    st.success(
        f"🏆 BEST MARKET: {best_market['Market']} | "
        f"Net Realisation: ₹{best_market['Net Realisation (₹/kg)']:.2f}/kg"
    )

    st.header("📈 Price Trend")

    price_data = {
        "Day": [
            "Day 1",
            "Day 2",
            "Day 3",
            "Day 4",
            "Day 5"
        ],
        "Price (₹/kg)": [
            18,
            18.5,
            19,
            20,
            21
        ]
    }

    price_df = pd.DataFrame(price_data)

    st.line_chart(
        price_df.set_index("Day")
    )

    latest_price = price_df["Price (₹/kg)"].iloc[-1]
    previous_price = price_df["Price (₹/kg)"].iloc[-2]

    if latest_price > previous_price:

        st.success(
            "📈 PRICE IS RISING → WAIT A LITTLE / WATCH THE MARKET"
        )

    else:

        st.warning(
            "📉 PRICE IS NOT RISING → CONSIDER SELLING"
        )

    st.write(
        f"Current observed price: ₹{latest_price}/kg"
    )


# ---------------- BUYER & DEALS ----------------

elif page == "🤝 Buyer & Deals":

    st.title("🤝 Buyer Matching & Deals")

    st.header("🏢 Verified Buyers")

    buyer_data = {
        "Buyer": [
            "AgroFresh Foods",
            "Delhi Food Processing Ltd.",
            "Krishi Retail Hub",
            "FreshKart Wholesale"
        ],
        "Crop": [
            "Potato",
            "Potato",
            "Wheat",
            "Potato"
        ],
        "Required Quantity (kg)": [
            500,
            1000,
            300,
            750
        ],
        "Offer (₹/kg)": [
            19,
            21,
            23,
            20
        ],
        "Location": [
            "Agra",
            "Delhi",
            "Mathura",
            "Agra"
        ],
        "Verified": [
            "✅ Yes",
            "✅ Yes",
            "✅ Yes",
            "✅ Yes"
        ]
    }

    buyer_df = pd.DataFrame(buyer_data)

    selected_crop = st.selectbox(
        "Select Crop",
        ["Potato", "Wheat", "Tomato", "Onion", "Rice"]
    )

    suitable_buyers = buyer_df[
        buyer_df["Crop"] == selected_crop
    ]

    st.dataframe(
        suitable_buyers,
        use_container_width=True
    )

    st.divider()

    st.header("💰 Create Buyer Offer")

    buyer = st.selectbox(
        "Select Buyer",
        buyer_df["Buyer"].tolist()
    )

    crop_name = st.selectbox(
        "Crop",
        ["Potato", "Wheat", "Tomato", "Onion", "Rice"]
    )

    quantity = st.number_input(
        "Quantity (kg)",
        min_value=1,
        value=500
    )

    offer_price = st.number_input(
        "Buyer Offer Price (₹/kg)",
        min_value=1.0,
        value=20.0
    )

    total_value = quantity * offer_price

    st.write("**Total Deal Value:** ₹", f"{total_value:,.2f}")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("✅ ACCEPT OFFER"):

            st.success(
                "🎉 Offer Accepted! Deal Created Successfully."
            )

    with col2:

        if st.button("❌ REJECT OFFER"):

            st.error("Offer Rejected.")


# ---------------- LOGISTICS ----------------

elif page == "🚚 Logistics":

    st.title("🚚 Transport & Logistics")

    st.write(
        "Plan transportation and storage after the crop is sold."
    )

    col1, col2 = st.columns(2)

    with col1:

        transporter = st.selectbox(
            "Select Transporter",
            [
                "Agra Transport Services",
                "Kisan Logistics",
                "FarmMove Transport"
            ]
        )

        distance = st.number_input(
            "Distance to Buyer (km)",
            min_value=1,
            value=50
        )

    with col2:

        transport_rate = st.number_input(
            "Transport Cost (₹ per km)",
            min_value=1.0,
            value=20.0
        )

        storage = st.selectbox(
            "Storage Required?",
            [
                "No",
                "Yes - Cold Storage",
                "Yes - Warehouse"
            ]
        )

    transport_cost = distance * transport_rate

    if storage == "No":
        storage_cost = 0
    else:
        storage_cost = 1000

    total_logistics = transport_cost + storage_cost

    st.header("📦 Logistics Summary")

    st.write("**Transporter:**", transporter)
    st.write("**Distance:**", distance, "km")
    st.write(
        "**Transport Cost:** ₹",
        f"{transport_cost:,.0f}"
    )
    st.write("**Storage:**", storage)
    st.write(
        "**Storage Cost:** ₹",
        f"{storage_cost:,.0f}"
    )

    st.success(
        f"🚛 TOTAL LOGISTICS COST: ₹{total_logistics:,.0f}"
    )

    if st.button("🚛 CONFIRM LOGISTICS"):

        st.success(
            "✅ Logistics plan created successfully!"
        )


# ---------------- PAYMENTS ----------------

elif page == "💰 Payments":

    st.title("💰 Payment Tracking")

    st.write(
        "Track the complete transaction from delivery to payment."
    )

    col1, col2 = st.columns(2)

    with col1:

        deal_amount = st.number_input(
            "Deal Amount (₹)",
            min_value=0,
            value=20000
        )

        delivery_status = st.selectbox(
            "Delivery Status",
            [
                "Pending",
                "Picked Up",
                "Delivered"
            ]
        )

    with col2:

        payment_status = st.selectbox(
            "Payment Status",
            [
                "Payment Pending",
                "Payment Processing",
                "Payment Received"
            ]
        )

        transaction_id = st.text_input(
            "Transaction ID",
            value="KM-2026-001"
        )

    st.header("📋 Transaction Summary")

    st.write("**Transaction ID:**", transaction_id)
    st.write(
        "**Deal Amount:** ₹",
        f"{deal_amount:,.2f}"
    )
    st.write("**Delivery:**", delivery_status)
    st.write("**Payment:**", payment_status)

    if payment_status == "Payment Received":

        st.success("✅ PAYMENT RECEIVED")

    elif payment_status == "Payment Processing":

        st.warning("⏳ PAYMENT IS PROCESSING")

    else:

        st.error("⚠️ PAYMENT PENDING")

    if st.button("💳 UPDATE TRANSACTION"):

        st.success(
            "✅ Transaction status updated successfully!"
        )


# ---------------- GRIEVANCES ----------------

elif page == "⚠️ Grievances":

    st.title("⚠️ Grievance & Dispute Support")

    st.write(
        "Farmers can report transaction-related problems."
    )

    grievance_type = st.selectbox(
        "Select Problem",
        [
            "Payment Not Received",
            "Quantity Mismatch",
            "Quality Dispute",
            "Transport Problem",
            "Buyer Issue"
        ]
    )

    transaction_id = st.text_input(
        "Transaction ID",
        value="KM-2026-001"
    )

    description = st.text_area(
        "Describe Your Problem",
        placeholder="Explain the issue here..."
    )

    if st.button("📢 SUBMIT GRIEVANCE"):

        if description.strip() == "":

            st.warning(
                "Please describe the problem first."
            )

        else:

            st.success(
                "✅ Grievance submitted successfully!"
            )

            st.write(
                "**Grievance Type:**",
                grievance_type
            )

            st.write(
                "**Transaction ID:**",
                transaction_id
            )

            st.write(
                "**Status:** 🟡 Under Review"
            )


# ---------------- ADMIN DASHBOARD ----------------

elif page == "🛠️ Admin Dashboard":

    st.title("🛠️ Admin Dashboard")

    st.write(
        "Monitor the overall Kisan Market platform."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🌾 Crop Lots", "128")

    with col2:
        st.metric("🏢 Verified Buyers", "46")

    with col3:
        st.metric("🤝 Active Deals", "32")

    with col4:
        st.metric("⚠️ Pending Grievances", "7")

    st.header("📊 Platform Overview")

    admin_data = {
        "Category": [
            "Crop Lots",
            "Verified Buyers",
            "Active Deals",
            "Completed Payments",
            "Pending Grievances"
        ],
        "Count": [
            128,
            46,
            32,
            25,
            7
        ]
    }

    admin_df = pd.DataFrame(admin_data)

    st.bar_chart(
        admin_df.set_index("Category")
    )

    st.header("🔍 Admin Actions")

    admin_action = st.selectbox(
        "Select Action",
        [
            "Verify Buyer",
            "Review Grievance",
            "Monitor Transaction",
            "View Market Activity"
        ]
    )

    if st.button("OPEN ADMIN ACTION"):

        st.success(
            f"✅ {admin_action} section opened."
        )
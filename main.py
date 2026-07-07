async def monitor():
    await send_alert(
        "✅ Bot Started Successfully",
        "https://railway.app",
        True
    )

    while True:
        with open(PRODUCTS_FILE, "r") as f:
            data = json.load(f)

        for product in data["products"]:

            if product["store"] == "amazon":
                result = check_amazon(product["url"])

            elif product["store"] == "flipkart":
                result = check_flipkart(product["url"])

            else:
                continue

            if result["stock"]:
                await send_alert(
                    result["title"],
                    result["url"],
                    True
                )

        await asyncio.sleep(CHECK_INTERVAL)

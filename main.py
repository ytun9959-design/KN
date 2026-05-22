import asyncio
import knobe  # ခုနက ရလာတဲ့ .so ဖိုင်ကို import လုပ်တာပါ

if __name__ == "__main__":
    try:
        # knobe.py ထဲက main() function ကို ခေါ်သုံးခြင်း
        asyncio.run(knobe.main())
    except KeyboardInterrupt:
        print("\n[!] Program stopped.")

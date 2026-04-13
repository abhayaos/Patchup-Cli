#!/usr/bin/env python3

import os
import sys
import time

def banner():
    print("=" * 40)
    print(" 💔 PATCHUP CLI TOOL 💔 ")
    print("=" * 40)
    time.sleep(0.5)

def main():
    banner()
    
    try:
        name = input("\nEnter name: ").strip()

        if not name:
            print("\n❌ Name cannot be empty!")
            sys.exit()

        print("\n⏳ Generating message...\n")
        time.sleep(1)

        result = f"Aau {name} patchup hana bhanya 💕"
        
        print("✨ Output:")
        print(result)
        print("\n" + "=" * 40)

    except KeyboardInterrupt:
        print("\n\n👋 Exiting...")
        sys.exit()

if __name__ == "__main__":
    main()

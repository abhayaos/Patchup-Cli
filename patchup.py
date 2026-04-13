#!/usr/bin/env python3

import argparse
import random
import sys
import time

# 🎨 Colors
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

# 💬 Messages
def get_messages(name):
    return {
        "classic": [
            f"Aau {name} patchup hana bhanya 💕",
        ],
        "emotional": [
            f"{name}… aba jhagada pugyo 😔 patchup gara na",
            f"{name}, timi bina sab empty xa 💔 patchup pls",
        ],
        "funny": [
            f"{name} lai bolau 😭 ego side ma rakhera patchup gara",
            f"{name} vs ego = ego haros, patchup jeetos 😂",
        ],
        "attitude": [
            f"{name}, last chance ho 😤 patchup gara natra block",
            f"{name} ko lagi ma nai aauxu, patchup finalize gara 🔥",
        ]
    }

# 🧠 Core Logic
def generate(name, style):
    messages = get_messages(name)

    if style not in messages:
        print(f"{Colors.RED}❌ Invalid style! Use: classic, emotional, funny, attitude{Colors.RESET}")
        sys.exit(1)

    return random.choice(messages[style])

# 🎬 Banner
def banner():
    print(f"""{Colors.CYAN}
========================================
        💔 PATCHUP CLI TOOL 💔
========================================
{Colors.RESET}""")

# 🚀 Main
def main():
    parser = argparse.ArgumentParser(
        description="Nepali Patchup CLI Tool 💕"
    )

    parser.add_argument(
        "-n", "--name",
        help="Name of the person",
        required=True
    )

    parser.add_argument(
        "-s", "--style",
        help="Message style",
        default="classic",
        choices=["classic", "emotional", "funny", "attitude"]
    )

    args = parser.parse_args()

    banner()

    print(f"{Colors.YELLOW}⏳ Generating patchup message...{Colors.RESET}")
    time.sleep(0.8)

    output = generate(args.name, args.style)

    print(f"\n{Colors.GREEN}✨ Result:{Colors.RESET}")
    print(f"{Colors.CYAN}{output}{Colors.RESET}\n")


if __name__ == "__main__":
    main()    main()

#!/usr/bin/env python3
"""
Test the improved kiro translator agent
"""

import subprocess
import sys


def test_translation(text, description):
    """Test a translation"""
    print(f"\n{'='*60}")
    print(f"Test: {description}")
    print(f"{'='*60}")
    print(f"Input text:\n{text}\n")

    result = subprocess.run(
        ["kiro-cli", "chat", "--no-interactive", "--agent=translator"],
        input=text,
        capture_output=True,
        text=True,
        timeout=30
    )

    if result.returncode != 0:
        print(f"❌ ERROR: Translation failed")
        print(f"stderr: {result.stderr}")
        return False

    translation = result.stdout.strip()
    print(f"Translation:\n{translation}\n")

    # Check if translation contains Chinese characters
    has_chinese = any('\u4e00' <= char <= '\u9fff' for char in translation)

    # Check for common error patterns
    has_error_patterns = any(pattern in translation.lower() for pattern in [
        "i understand you're",
        "i don't have access",
        "i can't provide",
        "however, i",
        "i noticed",
        "as an ai"
    ])

    if has_chinese and not has_error_patterns:
        print("✅ PASS: Translation contains Chinese and no error patterns")
        return True
    else:
        print("❌ FAIL:")
        if not has_chinese:
            print("  - Translation does not contain Chinese characters")
        if has_error_patterns:
            print("  - Translation contains error patterns")
        return False


def main():
    tests = [
        {
            "text": "Learn about comprehensive network security on AWS, focusing on integrating Amazon CloudFront, AWS WAF, Network Firewall, and Verified Access (AVA) for zero-trust architecture.",
            "description": "Network security abstract (previously failed in NET326)"
        },
        {
            "text": "AWS re:Invent 2025 - What's new with Amazon S3 (STG206)",
            "description": "Session title with re:Invent reference (previously failed in STG206)"
        },
        {
            "text": "Discover how to use Amazon VPC Lattice and AWS services to drive a smooth, step-by-step migration. Learn proven patterns for breaking down monoliths into microservices.",
            "description": "Technical content with AWS services"
        },
        {
            "text": "Amazon S3 consistently delivers new innovations to help you store, manage, analyze, and protect any amount of data for virtually any use case.",
            "description": "Product description"
        }
    ]

    passed = 0
    failed = 0

    for test in tests:
        if test_translation(test["text"], test["description"]):
            passed += 1
        else:
            failed += 1

    print(f"\n{'='*60}")
    print(f"Test Summary:")
    print(f"  Total: {len(tests)}")
    print(f"  ✅ Passed: {passed}")
    print(f"  ❌ Failed: {failed}")
    print(f"{'='*60}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

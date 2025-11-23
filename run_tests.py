#!/usr/bin/env python3
"""
Скрипт для быстрого запуска BDD тестов API Авито
"""

import subprocess
import sys
import os

def print_banner():
    print("=" * 60)
    print("ЗАПУСК BDD ТЕСТОВ API АВИТО")
    print("=" * 60)

def check_dependencies():
    try:
        import pytest
        import requests
        import pytest_bdd
        print("[OK] Все зависимости установлены")
        return True
    except ImportError as e:
        print(f"[ERROR] Отсутствуют зависимости: {e}")
        print("Установите: pip install -r requirements.txt")
        return False

def run_bdd_tests():
    print("\nЗапуск BDD тестов...")
    
    if not os.path.exists('avito_api.feature'):
        print("[ERROR] Файл advertisements_api.feature не найден!")
        return 1
    
    cmd = [
        sys.executable, "-m", "pytest",
        "test_bdd.py", 
        "-v",
        "-s",
        "--html=report.html",
        "--self-contained-html",
    ]
    
    print(f"Команда: {' '.join(cmd)}")
    print("-" * 60)
    
    result = subprocess.run(cmd)
    
    print("-" * 60)
    if result.returncode == 0:
        print("[SUCCESS] Все тесты пройдены")
    else:
        print("[FAILED] Некоторые тесты не прошли")
    
    print(f"Отчет: file://{os.path.abspath('report.html')}")
    return result.returncode

def main():
    print_banner()
    
    if not check_dependencies():
        return 1
    
    return run_bdd_tests()

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
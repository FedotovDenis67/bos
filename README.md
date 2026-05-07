# bos
alt-fstek-audit

# Файлы эксперимента

- `arp_watch.py` – Скрипт для обнаружения ARP-spoofing (MITRE T1040) на ОС Альт. Использует библиотеку Scapy, логирует подмену MAC-адресов.

- `c2_beacon.sh` – Bash-скрипт для имитации C2-активности (MITRE T1071.001). Отправляет периодические POST-запросы на заданный IP (сервер Kali).

- `fstek-tailoring.xml` – Tailoring-файл для OpenSCAP. Создаёт профиль `fstek` на основе OSPP, адаптированный для требований ФСТЭК.

- `results_tailored.xml` – Результат сканирования ОС Альт по профилю `fstek` в формате ARF. Содержит детали проверок и итоговую статистику (Pass/Fail/Score).

import csv
from ics import Calendar, Event

def csv_to_ics(input_csv_file, output_ics_file):
    cal = Calendar()

    with open(input_csv_file, 'r', encoding='cp1251') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            person_name = row['Name']
            custom_name = row['Custom Name'] if 'Custom Name' in row else person_name
            time = row['Time']
            description = f"Person ID: {row['Person ID']}, Department: {row['Department']}"

            # Создаем два разных события для каждой записи с разными значениями Attendance Status
            # Первое событие с Status 'Present'
            event_present = Event()
            event_present.name = f"{person_name} - {custom_name} (Present)"
            event_present.begin = time
            event_present.description = f"{description}, Attendance Status: Present"
            cal.events.add(event_present)

            # Второе событие с Status 'Absent'
            event_absent = Event()
            event_absent.name = f"{person_name} - {custom_name} (Absent)"
            event_absent.begin = time
            event_absent.description = f"{description}, Attendance Status: Absent"
            cal.events.add(event_absent)

    with open(output_ics_file, 'w', encoding='utf-8') as icsfile:
        icsfile.writelines(cal)

if __name__ == "__main__":
    input_csv_file = "input.csv"  # Замените на имя вашего CSV файла
    output_ics_file = "output.ics"  # Замените на имя, которое вы хотите присвоить файлу .ics
    csv_to_ics(input_csv_file, output_ics_file)

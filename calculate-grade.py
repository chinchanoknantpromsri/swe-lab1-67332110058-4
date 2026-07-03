def calculate_grade(scores):
    # 1. ตรวจสอบว่า scores เป็น List และไม่ว่างเปล่า (ป้องกัน ZeroDivisionError)
    if not scores or not isinstance(scores, list):
        return "No data", 0

    # 2. ใช้ฟังก์ชัน sum() เพื่อหาผลรวม (สะอาดและเร็วกว่า)
    try:
        total = sum(scores)
    except TypeError:
        return "Invalid data in list", 0

    average = total / len(scores)

    # 3. การตัดเกรด (Logic เดิมถูกต้องแล้ว แต่เขียนให้กระชับได้)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# ทดสอบการใช้งาน
scores = [85, 92, 78, 88, 95]
grade, avg = calculate_grade(scores)
print(f"Average: {avg:.2f}, Grade: {grade}")

# ทดสอบกรณี List ว่าง
print(calculate_grade([]))

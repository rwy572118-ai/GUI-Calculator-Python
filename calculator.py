import tkinter as tk
from tkinter import messagebox

# 1. دالة منطق العمليات الحسابية
def on_click(button_text):
    current_text = entry.get()
    
    if button_text == "=":
        try:
            # حساب المعادلة المكتوبة في الشاشة
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            # معالجة خطأ القسمة على صفر
            messagebox.showerror("خطأ", "لا يمكن القسمة على صفر")
            entry.delete(0, tk.END)
        except Exception:
            # معالجة أي أخطاء رياضية أخرى
            messagebox.showerror("خطأ", "عملية غير صالحة")
            entry.delete(0, tk.END)
            
    elif button_text == "C":
        # مسح الشاشة بالكامل
        entry.delete(0, tk.END)
    else:
        # إضافة الرقم أو الرمز المكتوب على الزر إلى الشاشة
        entry.insert(tk.END, button_text)

# 2. إعداد النافذة الرئيسية
root = tk.Tk()
root.title("آلةرؤى ذكية")
root.geometry("350x450") # تحديد حجم مناسب للنافذة

# 3. شاشة العرض (Entry)
entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# 4. قائمة الأزرار وترتيبها
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# 5. توزيع الأزرار باستخدام حلقة تكرار (Loop)
row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: on_click(x)
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
              command=action).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# 6. جعل الواجهة مرنة (تتمدد مع تكبير النافذة)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
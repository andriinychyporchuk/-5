def format_text(input_file, output_file, max_line_length):
    try:
       
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        words = text.split()

        formatted_text = ''

        current_line_length = 0
        for word in words:
            if current_line_length + len(word) + 1 <= max_line_length:
                
                formatted_text += word + ' '
                current_line_length += len(word) + 1
            else:
               
                formatted_text += '\n' + word + ' '
                current_line_length = len(word) + 1

        
        with open(output_file, 'w', encoding='utf-8') as file:
            
            file.write(formatted_text)

        print(f"Текст був відформатований та збережений  {output_file}")

    
    except Exception as e:
        print(f"Виникла помилка: {e}")

def get_max_line_length():
    while True:
        try:
            
            max_line_length = int(input("Введіть максимальну довжину рядка: "))
            return max_line_length
        except ValueError:
            print("Неправильний ввід.")

input_file_path = r'D:\1234\111.txt'
output_file_path = r'D:\1234\111_formatted.txt'

while True:
    max_line_length = get_max_line_length()

    format_text(input_file_path, output_file_path, max_line_length)

    user_input = input("Щоб ввести нове число, натисніть Enter. Для виходу введіть 'Q': ")
    if user_input.upper() == 'Q':
        break 
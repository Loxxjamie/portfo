from flask import Flask, render_template ,url_for ,redirect , request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<page_name>.html')
def render_page(page_name):
    return render_template(f"{page_name}.html")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() 
            write_to_csv(data)  # <-- HERE the function is called
            username=data.get('email')
            return redirect(url_for('render_page', page_name='thank_you', name=username))
        except:
            return 'did not save to database.try again'
    else:
        return "something went wrong"

    
def save_to_file(data):
    print("Saving:", data)   # DEBUG
    file_path = r"C:\\Users\\HP\Desktop\\OOP\web development\\web server\\database.txt"
    with open(file_path, mode='a') as file:  # 'a' = append mode
        email = data['email']
        subject = data['subject']
        message = data['message']
        # message = data.get('message')
        file.write(f"\n{email}, {subject}, {message}\n")

def write_to_csv(data):
    print("Saving:", data)   # DEBUG
    file_path = r"C:\\Users\\HP\Desktop\\OOP\web development\\web server\\database.csv"
    with open(file_path, mode='a',newline='') as database:  # 'a' = append mode
        email = data['email']
        subject = data['subject']
        message = data['message']
        # message = data.get('message')
        csv_writer=csv.writer(database,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 取的前端 input的值
        sex = request.form['sex']
        height = float(request.form['Height'])
        weight = float(request.form['Weight'])
        # print(height, weight)
        # print(sex)
        
        # 將height從公分轉換成公尺
        height_m = height / 100

        bmi = round(weight / (height_m ** 2), 1)

        # 判斷是 BMI 為過重、輕度肥胖、中度肥胖、重度肥胖等等...
     
        result = '健康體位'
        if bmi < 18.5:
            result = '體重過輕'
        elif 24 <= bmi < 27:
            result = '過重'
        elif 27 <= bmi < 30:
            result = '輕度肥胖'
        elif 30 <= bmi < 35:
            result = '中度肥胖'
        elif bmi >= 35:
            result = '重度肥胖'

        if sex == 'male':
            ideal_weight = (height - 80) * 0.7
        else:
            ideal_weight = (height - 70) * 0.6
        return render_template('index.html', height=height, weight=weight, bmi=bmi, result=result, ideal_weight=ideal_weight)
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
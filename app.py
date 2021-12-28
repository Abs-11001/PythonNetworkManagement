from flask import Flask, request, render_template
import os
import json
app = Flask(__name__)

# falsk 项目配置
app.config['JSON_AS_ASCII'] = False
noExistAccount = "查询不到数据，请检查是否存在账户或是否开启打卡或是否绑定账号"


@app.route('/')
def hello_world():
    return '欢迎访问Flask轻量级框架!'


@app.route("/register", methods=['GET', 'POST'])
def register():
    # return ("注册界面")
    if request.method == "POST":
        user = request.form.get("user")
        psd = request.form.get("psd")
        user_name = request.form.get("user_name")
        print(user_name)

        info = {}
        if not os.path.exists('assets/config/'):
            os.mkdir('assets/config/')
        try:
            with open("assets/config/account.json", "r", encoding='utf-8') as file:
                info = json.load(file)
        except:
            pass
        with open("assets/config/account.json", "w", encoding='utf-8') as file:
            info[user] = {"user_name": user_name, "psd": psd}
            json.dump(info, file)
        return {'sta': "注册成功"}

    return render_template('register.html')

    # if not cookie:
    #     return {'sta': noExistAccount}
    # res = checkInFun(cookie)
    # return {'sta': res}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7878, debug=True)

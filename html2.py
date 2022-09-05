import cgitb,io,sys

cgitb.enable()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print ("Content-Type: text/html; charset=UTF-8;\n\n")

page_data = {}
page_data['site_title'] = 'sample'
page_data['page_title'] = 'Pythonサンプルページ'
page_data['header'] = '<h1>sample</h1>'
page_data['contents'] = '<h2>'+ page_data['page_title'] +'</h2><p>Pythonを使って作成したサンプルページです</p>'
page_data['sidebar'] = '<p>サイドバー</p>'
page_data['footer'] = '<p>フッター</p>'

with webbrowser.open('html2.html','r') as file:
    html = file.read()
file.closed

for key, value in page_data.items():
    html = html.replace('{% ' + key + ' %}', value)


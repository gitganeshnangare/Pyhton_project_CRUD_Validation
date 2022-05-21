from config.config import *
from model.product import Product


@app.route('/')
def welcome_page():
    return render_template('index.html')


productList=[]
@app.route('/save/product',methods=['POST','GET'])
def add_product():
    message=''
    if request.method=='POST':
        formdata=request.form
        pId=int(formdata.get('pid'))
        isDuplicate=False
        for prod in productList:
            if prod.Product_ID==pId:
                prod.Product_Name=formdata.get('pname')
                prod.Product_Vendor = formdata.get('pven')
                prod.Product_Price = float(formdata.get('ppr'))
                prod.Product_Qty = int(formdata.get('pqty'))

                isDuplicate=True
                break
        if isDuplicate:
            message = 'Product Succefully updated ..'

        else:
            pId=formdata.get('pid')
            pNm = formdata.get('pname')
            pVd = formdata.get('pven')
            pQt = formdata.get('pqty')
            pPn =formdata.get('ppr')
            prod=Product(prid=pId,prnm=pNm,price=pPn,prven=pVd,prqty=pQt)
            productList.append(prod)
            message='Product Added Succesfully '


    return render_template('add_product.html',message=message,product=Product())


@app.route('/show/product')
def save_product():
    return render_template('show_product.html',productlist=productList)

@app.route('/edit/product<int:pId>',methods=['GET'])
def edit_product(pId):
    product=None
    for prod in productList:
        if prod.Product_ID==pId:
            product=prod
    return render_template('add_product.html',product=product)

@app.route('/delete/product<int:pId>')
def delete_product(pId):
    for prod in productList:
        # prod=Product
        if prod.Product_ID==pId:
            productList.remove(prod)
            break
    return render_template('show_product.html',productlist=productList)

@app.route('/search/product',methods=['GET','POST'])
def search_product():
    if request.method=="POST":
        formdata=request.form
        pId=int(formdata.get('pId'))
        for prod in productList:
            if prod.Product_ID==pId:
                return render_template('search_product.html',product=prod)
    return render_template('search_product.html',productlist=None)



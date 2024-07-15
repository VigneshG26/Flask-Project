from flask import Flask, render_template



app = Flask(__name__)

Toys = [
    {
        'id':1,
        'thumbnail': '../static/images/kids1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/kids1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Laptop = [
    {
        'id':1,
        'thumbnail': '../static/images/laptop1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/laptop1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Shoes = [
    {
        'id':1,
        'thumbnail': '../static/images/shoes1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/shoes1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Mobile = [
    {
        'id':1,
        'thumbnail': '../static/images/mobile1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/mobile1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Headphones = [
    {
        'id':1,
        'thumbnail': '../static/images/headphones1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/headphones1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Women = [
    {
        'id':1,
        'thumbnail': '../static/images/women1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/women1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Speaker = [
    {
        'id':1,
        'thumbnail': '../static/images/speaker1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/speaker1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
CollegeBag = [
    {
        'id':1,
        'thumbnail': '../static/images/cbag1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/cbag1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Handbags = [
    {
        'id':1,
        'thumbnail': '../static/images/hbags1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/hbags1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Men = [
    {
        'id':1,
        'thumbnail': '../static/images/men1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/men1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
TShirt = [
    {
        'id':1,
        'thumbnail': '../static/images/tshirt1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/tshirt1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Watch = [
    {
        'id':1,
        'thumbnail': '../static/images/watch1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/watch1.png',
        'brand':'funskool',
        'offer_pice':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products/<name>')
def products(name):
    if name == 'Toys':
        categories = Toys
    elif name =='Laptop':
        categories = Laptop
    elif name =='Shoes':
        categories = Shoes
    elif name =='Mobile':
        categories = Mobile
    elif name =='Headphones':
        categories = Headphones
    elif name =='Women':
        categories = Women
    elif name =='Speaker':
        categories = Speaker
    elif name =='CollegeBag':
        categories = CollegeBag
    elif name =='Handbags':
        categories = Handbags
    elif name =='Men':
        categories = Men
    elif name =='T-shirts':
        categories = TShirt
    elif name =='Watch':
        categories = Watch
    return render_template('specific_products.html',categories = categories, title = name)



if __name__ == '__main__':
    app.run(debug=True)
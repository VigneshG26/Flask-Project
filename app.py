from flask import Flask, render_template



app = Flask(__name__)

Toys = [
    {
        'id':1,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/toys/ukids2.jpg',
        'brand':'funskool',
        'smalld': 'Hot Wheels',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':3,
        'thumbnail': '../static/images/toys/ukids3.png',
        'brand':'funskool',
        'smalld': 'Toy Car',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':4,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':5,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':6,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':7,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':8,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':9,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':10,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':11,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':12,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':13,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':14,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':15,
        'thumbnail': '../static/images/toys/ukids1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Laptop = [
    {
        'id':1,
        'thumbnail': '../static/images/laptops/ulaptop1.png',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/laptops/ulaptop2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/laptops/ulaptop1.png',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/laptops/ulaptop2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/laptops/ulaptop1.png',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/laptops/ulaptop2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Shoes = [
    {
        'id':1,
        'thumbnail': '../static/images/shoes/ushoes1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/shoes/ushoes2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
     {
        'id':2,
        'thumbnail': '../static/images/shoes/ushoes3.png',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
     {
        'id':1,
        'thumbnail': '../static/images/shoes/ushoes1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/shoes/ushoes2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
     {
        'id':2,
        'thumbnail': '../static/images/shoes/ushoes3.png',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Mobile = [
    {
        'id':1,
        'thumbnail': '../static/images/mobiles/umobile1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/mobiles/umobile2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':3,
        'thumbnail': '../static/images/mobiles/umobile3.png',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/mobiles/umobile1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/mobiles/umobile2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':3,
        'thumbnail': '../static/images/mobiles/umobile3.png',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Headphones = [
    {
        'id':1,
        'thumbnail': '../static/images/headphones/uheadphones1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/headphones/uheadphones2.png',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/headphones/uheadphones1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/headphones/uheadphones2.png',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/headphones/uheadphones1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/headphones/uheadphones2.png',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Women = [
    {
        'id':1,
        'thumbnail': '../static/images/women/uwomen1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/women/uwomen2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/women/uwomen1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/women/uwomen2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/women/uwomen1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/women/uwomen2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Speaker = [
    {
        'id':1,
        'thumbnail': '../static/images/speakers/uspeaker1.jpeg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/speakers/uspeaker2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/speakers/uspeaker1.jpeg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/speakers/uspeaker2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/speakers/uspeaker1.jpeg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/speakers/uspeaker2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
CollegeBag = [
    {
        'id':1,
        'thumbnail': '../static/images/collegebags/ucbag1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/collegebags/ucbag2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/collegebags/ucbag1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/collegebags/ucbag2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/collegebags/ucbag1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/collegebags/ucbag2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Handbags = [
    {
        'id':1,
        'thumbnail': '../static/images/handbags/uhbags1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/handbags/uhbags2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/handbags/uhbags1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/handbags/uhbags2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/handbags/uhbags1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/handbags/uhbags2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Men = [
    {
        'id':1,
        'thumbnail': '../static/images/men/umen1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/men/umen2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
     {
        'id':1,
        'thumbnail': '../static/images/men/umen1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/men/umen2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
     {
        'id':1,
        'thumbnail': '../static/images/men/umen1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/men/umen2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
TShirt = [
    {
        'id':1,
        'thumbnail': '../static/images/tshirts/utshirt1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/tshirts/utshirt2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/tshirts/utshirt1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/tshirts/utshirt2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/tshirts/utshirt1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/tshirts/utshirt2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    }
]
Watch = [
    {
        'id':1,
        'thumbnail': '../static/images/watches/uwatch1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/watches/uwatch2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/watches/uwatch1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/watches/uwatch2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':1,
        'thumbnail': '../static/images/watches/uwatch1.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
        'actula_price':'₹1,000',
        'offer_percentage': '50% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/watches/uwatch2.jpg',
        'brand':'funskool',
        'smalld': 'Teddy Bear',
        'offer_price':'₹500',
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
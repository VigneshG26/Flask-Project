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
        'brand':'LayOneX',
        'smalld': 'College Bags',
        'offer_price':'₹600',
        'actula_price':'₹1,000',
        'offer_percentage': '40% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/collegebags/ucbag2.jpg',
        'brand':'KNS',
        'smalld': 'College Bags',
        'offer_price':'₹666',
        'actula_price':'₹1,000',
        'offer_percentage': '33% off'
    },
    {
        'id':3,
        'thumbnail': '../static/images/collegebags/cbag3.jpeg',
        'brand':'Right Choice',
        'smalld': 'College Bags',
        'offer_price':'₹450',
        'actula_price':'₹500',
        'offer_percentage': '10% off'
    },
    {
        'id':4,
        'thumbnail': '../static/images/collegebags/cbag4.jpeg',
        'brand':'KNS',
        'smalld': 'College Bags',
        'offer_price':'₹750',
        'actula_price':'₹1,000',
        'offer_percentage': '25% off'
    },
    {
        'id':5,
        'thumbnail': '../static/images/collegebags/cbag5.jpg',
        'brand':'American Tourist',
        'smalld': 'College Bags',
        'offer_price':'₹1,040',
        'actula_price':'₹1,300',
        'offer_percentage': '20% off'
    },
    {
        'id':6,
        'thumbnail': '../static/images/collegebags/cbag6.jpg',
        'brand':'American Tourist',
        'smalld': 'College Bags',
        'offer_price':'₹1,870',
        'actula_price':'₹2,200',
        'offer_percentage': '15% off'
    },
    {
        'id':7,
        'thumbnail': '../static/images/collegebags/cbag7.avif',
        'brand':'Sky Bags',
        'smalld': 'College Bags',
        'offer_price':'₹1,125',
        'actula_price':'₹1,250',
        'offer_percentage': '10% off'
    },
    {
        'id':8,
        'thumbnail': '../static/images/collegebags/cbag8.jpg',
        'brand':'Sky Bags',
        'smalld': 'College Bags',
        'offer_price':'₹900',
        'actula_price':'₹1,500',
        'offer_percentage': '40% off'
    },
    {
        'id':9,
        'thumbnail': '../static/images/collegebags/cbag9.jpg',
        'brand':'Wilf Craft',
        'smalld': 'College Bags',
        'offer_price':'₹1,160',
        'actula_price':'₹1,550',
        'offer_percentage': '25% off'
    },
    {
        'id':10,
        'thumbnail': '../static/images/collegebags/cbag10.jpeg',
        'brand':'Wilf Craft',
        'smalld': 'College Bags',
        'offer_price':'₹1,120',
        'actula_price':'₹1,400',
        'offer_percentage': '20% off'
    },
    {
        'id':11,
        'thumbnail': '../static/images/collegebags/cbag11.jpg',
        'brand':'Tommy Hilfiger',
        'smalld': 'College Bags',
        'offer_price':'₹1,955',
        'actula_price':'₹2,300',
        'offer_percentage': '15% off'
    },
    {
        'id':12,
        'thumbnail': '../static/images/collegebags/cbag12.jpg',
        'brand':'Tommy Hilfiger',
        'smalld': 'College Bags',
        'offer_price':'₹990',
        'actula_price':'₹1,100',
        'offer_percentage': '10% off'
    },
    {
        'id':13,
        'thumbnail': '../static/images/collegebags/cbag13.jpg',
        'brand':'Puma',
        'smalld': 'College Bags',
        'offer_price':'₹1,275',
        'actula_price':'₹1,700',
        'offer_percentage': '25% off'
    },
    {
        'id':14,
        'thumbnail': '../static/images/collegebags/cbag14.jpg',
        'brand':'Puma',
        'smalld': 'College Bags',
        'offer_price':'₹1,351',
        'actula_price':'₹1,930',
        'offer_percentage': '30% off'
    },
    {
        'id':15,
        'thumbnail': '../static/images/collegebags/cbag15.jpg',
        'brand':'Reebok',
        'smalld': 'College Bags',
        'offer_price':'₹1,334',
        'actula_price':'₹1,450',
        'offer_percentage': '8% off'
    },
    {
        'id':16,
        'thumbnail': '../static/images/collegebags/cbag16.jpg',
        'brand':'Reebok',
        'smalld': 'College Bags',
        'offer_price':'₹954',
        'actula_price':'₹1,125',
        'offer_percentage': '16% off'
    },
    {
        'id':17,
        'thumbnail': '../static/images/collegebags/cbag17.jpg',
        'brand':'Ak Inter',
        'smalld': 'College Bags',
        'offer_price':'₹826',
        'actula_price':'₹1,180',
        'offer_percentage': '30% off'
    },
    {
        'id':18,
        'thumbnail': '../static/images/collegebags/cbag18.jpg',
        'brand':'Nike',
        'smalld': 'College Bags',
        'offer_price':'₹1,564',
        'actula_price':'₹1,840',
        'offer_percentage': '15% off'
    },
    {
        'id':19,
        'thumbnail': '../static/images/collegebags/cbag19.jpg',
        'brand':'Nike',
        'smalld': 'College Bags',
        'offer_price':'₹1,495',
        'actula_price':'₹1,625',
        'offer_percentage': '8% off'
    },
    {
        'id':20,
        'thumbnail': '../static/images/collegebags/cbag20.jpg',
        'brand':'Asian Bags',
        'smalld': 'College Bags',
        'offer_price':'₹920',
        'actula_price':'₹1,150',
        'offer_percentage': '20% off'
    }
]
Handbags = [
    {
        'id':1,
        'thumbnail': '../static/images/handbags/uhbags1.jpg',
        'brand':'Herald',
        'smalld': 'Hand Bag',
        'offer_price':'₹850',
        'actula_price':'₹1,000',
        'offer_percentage': '15% off'
    },
    {
        'id':2,
        'thumbnail': '../static/images/handbags/uhbags2.jpg',
        'brand':'Herald',
        'smalld': 'Hand Bag',
        'offer_price':'₹792',
        'actula_price':'₹900',
        'offer_percentage': '12% off'
    },
    {
        'id':3,
        'thumbnail': '../static/images/handbags/hbags3.png',
        'brand':'Madewell',
        'smalld': 'Hand Bag',
        'offer_price':'₹1,025',
        'actula_price':'₹1,250',
        'offer_percentage': '18% off'
    },
    {
        'id':4,
        'thumbnail': '../static/images/handbags/hbags4.jpg',
        'brand':'Madewell',
        'smalld': 'Hand Bag',
        'offer_price':'₹899',
        'actula_price':'₹1,040',
        'offer_percentage': '14% off'
    },
    {
        'id':5,
        'thumbnail': '../static/images/handbags/hbags5.jpg',
        'brand':'Cocolyn',
        'smalld': 'Hand Bag',
        'offer_price':'₹784',
        'actula_price':'₹980',
        'offer_percentage': '20% off'
    },
    {
        'id':6,
        'thumbnail': '../static/images/handbags/hbags6.png',
        'brand':'Cocolyn',
        'smalld': 'Hand Bag',
        'offer_price':'₹510',
        'actula_price':'₹600',
        'offer_percentage': '15% off'
    },
    {
        'id':7,
        'thumbnail': '../static/images/handbags/hbags7.jpg',
        'brand':'Kangaroo',
        'smalld': 'Hand Bag',
        'offer_price':'₹2,385',
        'actula_price':'₹2,840',
        'offer_percentage': '16% off'
    },
    {
        'id':8,
        'thumbnail': '../static/images/handbags/hbags8.jpg',
        'brand':'Kangaroo',
        'smalld': 'Hand Bag',
        'offer_price':'₹2,288',
        'actula_price':'₹2,570',
        'offer_percentage': '11% off'
    },
    {
        'id':9,
        'thumbnail': '../static/images/handbags/hbags9.jpg',
        'brand':'Salvo',
        'smalld': 'Hand Bag',
        'offer_price':'₹699',
        'actula_price':'₹862',
        'offer_percentage': '19% off'
    },
    {
        'id':10,
        'thumbnail': '../static/images/handbags/hbags10.jpg',
        'brand':'Salvo',
        'smalld': 'Hand Bag',
        'offer_price':'₹1,156',
        'actula_price':'₹1,329',
        'offer_percentage': '13% off'
    },
    {
        'id':11,
        'thumbnail': '../static/images/handbags/hbags11.jpeg',
        'brand':'Berrylush',
        'smalld': 'Hand Bag',
        'offer_price':'₹990',
        'actula_price':'₹1,100',
        'offer_percentage': '10% off'
    },
    {
        'id':12,
        'thumbnail': '../static/images/handbags/hbags12.png',
        'brand':'Berrylush',
        'smalld': 'Hand Bag',
        'offer_price':'₹1,100',
        'actula_price':'₹1,250',
        'offer_percentage': '12% off'
    },
    {
        'id':13,
        'thumbnail': '../static/images/handbags/hbags13.jpg',
        'brand':'Caprese Callie',
        'smalld': 'Hand Bag',
        'offer_price':'₹899',
        'actula_price':'₹999',
        'offer_percentage': '11% off'
    },
    {
        'id':14,
        'thumbnail': '../static/images/handbags/hbags14.jpg',
        'brand':'Caprese Callie',
        'smalld': 'Hand Bag',
        'offer_price':'₹550',
        'actula_price':'₹620',
        'offer_percentage': '12% off'
    },
    {
        'id':15,
        'thumbnail': '../static/images/handbags/hbags15.jpg',
        'brand':'Jeep',
        'smalld': 'Hand Bag',
        'offer_price':'₹1,140',
        'actula_price':'₹1,200',
        'offer_percentage': '5% off'
    },
    {
        'id':16,
        'thumbnail': '../static/images/handbags/hbags16.png',
        'brand':'Allen Solly',
        'smalld': 'Hand Bag',
        'offer_price':'₹1,732',
        'actula_price':'₹2,165',
        'offer_percentage': '20% off'
    },
    {
        'id':17,
        'thumbnail': '../static/images/handbags/hbags17.jpg',
        'brand':'Allen Solly',
        'smalld': 'Hand Bag',
        'offer_price':'₹1,092',
        'actula_price':'₹1,199',
        'offer_percentage': '9% off'
    },
    {
        'id':18,
        'thumbnail': '../static/images/handbags/hbags18.jpg',
        'brand':'Michael Kors',
        'smalld': 'Hand Bag',
        'offer_price':'₹1,056',
        'actula_price':'₹1,200',
        'offer_percentage': '12% off'
    },
    {
        'id':19,
        'thumbnail': '../static/images/handbags/hbags19.jpg',
        'brand':'Michael Kors',
        'smalld': 'Hand Bag',
        'offer_price':'₹1,1360',
        'actula_price':'₹1,600',
        'offer_percentage': '15% off'
    },
    {
        'id':20,
        'thumbnail': '../static/images/handbags/hbags20.jpg',
        'brand':'Trava',
        'smalld': 'Hand Bag',
        'offer_price':'₹588',
        'actula_price':'₹700',
        'offer_percentage': '16% off'
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
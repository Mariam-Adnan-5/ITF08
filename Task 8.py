products=[]
number=0
while True:
    selection=int(input("1-Add new product\n2-Print product details\n3-Buy product\n4-Delet product\n"
                        "5-Exit\n Enteer your choice"))
    if selection==1:
        number+=1
        name=input("Enter Product Name: ")
        price=int(input("Enter Product Price: "))
        quantity=int(input("Enter Product Quantity:"))
        product={
            "id":number,
            "name":name,
            "price":price,
            "quantity":quantity}
        products.append(product)
        print("Product Added Successfully")
    elif selection==2:
        product_number=int(input("Enter product number"))
        for i in products:
            if i.get("id")==product_number:
                print(i)
                break
    elif selection==3:
        product_number=int(input("Enter product number"))
        product_qun=int(input("Enter product Quantity"))
        for i in products:
          if i.get("id") == product_number:
            updat=i.get("quantity") - product_qun
            i.update({"quantity":updat})
            break

    elif selection==4:
        product_number = int(input("Enter product number"))
        for i in products:
            if i.get("id") == product_number:
             del i
             break

    elif selection == 5:
        exit()

    else:
     print("Invailed input")


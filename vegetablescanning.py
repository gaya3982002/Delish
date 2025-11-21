import tensorflow as tf
import sys
import os


# Disable tensorflow compilation warnings
from tensorflow_core.contrib import slim

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

from time import strftime

from flask import *
from DBConnection import *

app = Flask(__name__)
app.secret_key="gvgj"


@app.route('/')
def login():
    return render_template("login_index.html")

@app.route('/index')
def index():
    return render_template("admin/index.html")


@app.route('/login_post', methods=['post'])
def login_post():
    username = request.form['textfield']
    password = request.form['textfield2']
    db=Database()
    qry="select * from login where Username='"+ username+"' and Password='"+password+"'"
    res=db.selectOne(qry)
    if res is not None :
        session['lid']=res['lid']
        if res['Type']=='admin' :
            return redirect('/admin_home')
        elif res['Type']=='shop':
            return redirect('/shop_home')
        else:
            return '''<script> alert ('invalid'); window.location="/"</script>'''
    else:
        return '''<script> alert ('invalid'); window.location="/"</script>'''

@app.route('/logout')
def logout():
    session['lid']=""
    return redirect('/')


@app.route('/admin_home')
def admin_home():
    if session['lid']!='':
        return render_template('admin/index.html')
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/admin_add_vegetables')
def admin_add_vegetables():
    if session['lid'] != '':
        return render_template("admin/Add vegetables.html")
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/add_veg_post',methods=['post'])
def add_veg_post():
    if session['lid'] != '':
        veg_name=request.form['textfield']
        veg_image=request.files['fileField']
        a="IMG"+strftime("%Y%m%d%H%M%S")+"jpg"
        veg_image.save("D:\\project\\New folder\\vegetablescanning\\static\\Vegetable\\"+a)
        path="/static/Vegetable/"+a
        db=Database()
        qry="INSERT INTO vegetables(Veg_name,Image)VALUES('"+veg_name+"','"+path+"')"
        res=db.insert(qry)
        return '''<script>alert('Successfully');window.location="/admin_add_vegetables"</script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_vegetables')
def view_vegetables():
    if session['lid'] != '':
        db=Database()
        qry="SELECT * FROM vegetables"
        res=db.select(qry)
        return render_template('admin/Viewvegetables.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_vegetable_post',methods=['post'])
def view_vegetables_post():
    if session['lid'] != '':
        vegetablename=request.form['textfield']
        db=Database()
        qry="SELECT * FROM vegetables WHERE Veg_name LIKE'"+vegetablename+"'"
        res=db.select(qry)
        return render_template('admin/Viewvegetables.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/admin_delete_vegetables/<id>')
def admin_delete_vegetables(id):
    if session['lid'] != '':
        db=Database()
        qry="DELETE FROM `vegetables` WHERE Veg_id='"+id+"'"
        res=db.delete(qry)
        return '''<script>alert('deleted successfully');window.location='/view_vegetables'</Script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/edit_vegetable/<id>')
def edit_vegetable(id):
    if session['lid'] != '':
        db=Database()
        qry = "SELECT * FROM vegetables  WHERE Veg_id='"+id+"'"
        res=db.selectOne(qry)
        return render_template('admin/edit vegetables.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/edit_vegetable_post',methods=['post'])
def edit_vegetable_post():
    if session['lid'] != '':
            id=request.form['id']
            veg_name = request.form['textfield']
            veg_image = request.files['fileField']
            a = "IMG" + strftime("%Y%m%d%H%M%S") + "jpg"
            veg_image.save("D:\\project\\New folder\\vegetablescanning\\static\\Vegetable\\" + a)
            path = "/static/Vegetable/" + a
            db=Database()
            if request.files!="None":
                if veg_image.filename!="":
                    qry="UPDATE vegetables SET Veg_name='"+ veg_name+"',image='"+path+"' WHERE Veg_id='"+id+"'"
                    res=db.update(qry)
                else:
                    qry = "UPDATE vegetables SET Veg_name='" + veg_name + "' WHERE Veg_id='" + id + "'"
                    res = db.update(qry)
            else:
                qry = "UPDATE vegetables SET Veg_name='" + veg_name + "' WHERE Veg_id='" + id + "'"
                res = db.update(qry)
            return  '''<script>alert('Edited successfully');window.location='/view_vegetables'</Script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''



@app.route('/admin_add_recipe')
def admin_add_recipe():
    if session['lid'] != '':

        return render_template('admin/AddRecipe.html')
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/add_recipe_post',methods=['post'])
def add_recipe_post():
    if session['lid'] != '':
        recipename=request.form['textfield']
        image=request.files['fileField']
        description=request.form['textarea']
        b="IMG"+strftime("%Y%m%d%H%M%S")+"jpg"
        image.save("D:\\project\\New folder\\vegetablescanning\\static\\Recipe\\"+b)
        path="/static/Recipe/"+b
        db=Database()
        qry="INSERT INTO recipe(Recipe_name,image,Description)VALUES('"+recipename+"','"+path+"','"+description+"')"
        res=db.insert(qry)
        session['rid']=str(res)
        print(session['rid'])
        return '''<script>alert('Successfully Added');window.location='/add_recipe_item'</script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/add_recipe_item')
def add_recipe_item():
    if session['lid'] != '':
        db=Database()
        qry="select * from vegetables"
        res=db.select(qry)
        return render_template("admin/add_recipiee_item.html",data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/add_recipe_item_post', methods=['POST'])
def add_recipe_item_post():
    if session['lid'] != '':
        db=Database()
        veg=request.form.getlist('checkbox')
        print()
        rid=session['rid']
        a=[]
        for b in veg:
            a.append(b)
            qry="INSERT INTO `recipe_item`(`Rec_id`,`Veg_id`) VALUES('"+rid+"','"+b+"')"
            res=db.insert(qry)
            print("hlooooooooooo")
        return '''<script>alert('Successfully Added');window.location='/view_recipe'</script>'''

    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_rec_item')
def view_rec_item():
    if session['lid'] != '':
        db=Database()
        qry="SELECT * FROM `recipe_item` INNER JOIN `vegetables` ON `recipe_item`.`Veg_id`=`vegetables`.`Veg_id` INNER JOIN `recipe` ON `recipe_item`.`Rec_item_id`=`recipe`.`Recipe_id`"
        res=db.select(qry)
        return render_template('admin/View_item.html', data=res)

    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/admin_delete_item/<id>')
def admin_delete_item(id):
    if session['lid'] != '':
        db=Database()
        qry="DELETE FROM `recipe_item` WHERE `Rec_item_id`='"+id+"'"
        res=db.delete(qry)
        return '''<script>alert('Deleted Successfully ');window.location='/view_recipe_item'</script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_approvestore')
def view_approvestore():
    if session['lid'] != '':
            db=Database()
            qry="SELECT * FROM store WHERE status='pending'"
            res=db.select(qry)
            return render_template("admin/View&ApproveStore.html", data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/search_store', methods=['post'])
def search_store():
    if session['lid'] != '':
        search = request.form['textfield']
        db = Database()
        qry = "SELECT * FROM store WHERE status='pending' and Store_name like '%"+search+"%'"
        res = db.select(qry)
        return render_template("admin/View&ApproveStore.html", data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/approve_store/<id>')
def approve_store(id):
    if session['lid'] != '':
        db=Database()
        qry="UPDATE store SET STATUS='approved' WHERE Store_id='"+id+"'"
        res=db.update(qry)
        return'''<script>alert("Approved succesfully");window.location='/view_approvestore'</script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/reject_store/<id>')
def reject_store(id):
    if session['lid'] != '':
        db=Database()
        qry="UPDATE store SET STATUS='rejected' WHERE Store_id='"+id+"'"
        print(qry)
        res=db.update(qry)
        return'''<script>alert("Rejected succesfully");window.location='/view_approvedstores'</script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_approvedstores')
def view_approvedstores():
    if session['lid'] != '':
        db=Database()
        qry="SELECT * FROM store WHERE status='approved'"
        res=db.select(qry)
        return render_template("admin/ViewApprovedStores.html",data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''
@app.route('/search_approved_Store', methods=['post'])
def search_approved_Store():
    if session['lid'] != '':
        search = request.form['textfield']
        db = Database()
        qry = "SELECT * FROM store WHERE status='approved' and Store_name like '"+search+"'"
        res = db.select(qry)
        return render_template('admin/ViewApprovedStores.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/View_Complaint')
def View_complaint():
    if session['lid'] != '':
        db=Database()
        qry="SELECT * FROM complaint INNER JOIN USER ON user.User_lid=complaint.User_lid"
        res=db.select(qry)
        return render_template('admin/ViewComplaint.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/complaintreply/<cid>')
def complaintreply(cid):
    if session['lid'] != '':
        db = Database()
        qry = "SELECT * FROM complaint INNER JOIN USER ON user.User_lid=complaint.User_lid where complaint.Comp_id='"+str(id)+"'"
        res = db.selectOne(qry)
        return render_template('admin/ComplaintReply.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/complaintreply_post',methods=['post'])
def complaintreply_post():
    if session['lid'] != '':
        cid=request.form['id']
        reply=request.form['textarea']
        db=Database()
        qry="update complaint set Reply='"+reply+"',Status='replied' where Comp_id='"+cid+"'"
        res=db.update(qry)
        return '''<script>alert("Replied succesfully");window.location='/View_Complaint'</script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''





@app.route('/search_complaint', methods=['post'])
def search_complaint():
    if session['lid'] != '':
        frm_date = request.form['textfield']
        to_date = request.form['textfield']
        db = Database()
        qry = "SELECT * FROM complaint INNER JOIN USER ON user.User_lid=complaint.User_lid where date BETWEEN '"+frm_date+"' and '"+to_date+"'"
        res = db.select(qry)
        return render_template('admin/ViewComplaint.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_item')
def view_item():
    if session['lid'] != '':
        db=Database()
        qry="SELECT item.*,vegetables.* FROM item INNER JOIN vegetables ON item.Veg_id=vegetables.Veg_id "
        res=db.select(qry)
        return render_template('admin/Viewitem.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/view_item_post',methods=['post'])
def view_item_post():
    if session['lid'] != '':
        name = request.form['textfield']
        db = Database()
        qry = "SELECT * FROM item WHERE NAME LIKE '%"+name+"%'"
        res=db.select(qry)
        return render_template('admin/Viewitem.html', data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/view_recipe')
def view_recipe():
    if session['lid'] != '':
        db = Database()
        qry = "SELECT * FROM recipe "
        res = db.select(qry)
        return render_template('admin/ViewRecipe.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_reciepee_items/<rid>')
def view_reciepee_items(rid):
    if session['lid'] != '':
        db=Database()
        qry="SELECT * FROM `recipe`INNER JOIN `recipe_item` ON `recipe`.`Recipe_id`=`recipe_item`.`Rec_id` INNER JOIN `vegetables` ON `recipe_item`.`Veg_id`=`vegetables`.`Veg_id` where `recipe_item`.`Rec_id`='"+rid+"' "
        res=db.select(qry)
        return render_template("admin/Viewreciepee_items.html",data=res)

    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/edit_recipe_item/<vid>')
def edit_recipe_item(vid):
    if session['lid'] != '':
        db=Database()
        qry2="SELECT * FROM `recipe_item` INNER JOIN `vegetables` ON `recipe_item`.`Veg_id`=`vegetables`.`Veg_id` WHERE `recipe_item`.`Rec_id`='"+vid+"'"
        res2=db.select(qry2)
        qry="select * from vegetables"
        res=db.select(qry)
        print(res)
        qry1="SELECT * FROM `recipe_item` INNER JOIN `vegetables` ON `recipe_item`.`Veg_id`=`vegetables`.`Veg_id` WHERE `recipe_item`.`Rec_id`='"+vid+"'"
        res1=db.selectOne(qry1)
        print(res1)
        return render_template("admin/edit_recipiee_item.html",data=res,data1=res1,data2=res2,vid=vid)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/edit_recipe_item_post', methods=['POST'])
def edit_recipe_item_post():
    if session['lid'] != '':
        db=Database()
        reciepee_id=request.form['riid']
        print(reciepee_id)
        veg=request.form.getlist('checkbox')
        # rid=session['rid']
        a=[]
        for b in veg:
            a.append(b)
            qry="INSERT INTO `recipe_item`(`Rec_id`,`Veg_id`) VALUES('"+reciepee_id+"','"+b+"')"
            res=db.insert(qry)
            print(a,"haiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        return '''<script>alert('Successfully Added');window.location='/view_recipe'</script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/remove_recipe_item/<vid>')
def remove_recipe_item(vid):
    if session['lid'] != '':
        db=Database()
        qry="DELETE FROM `recipe_item` WHERE `Veg_id`='"+vid+"'"
        res=db.delete(qry)
        return '''<script>alert('Removed Successfully');window.location='/view_recipe#hai'</script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''




@app.route('/view_recipe_post',methods=['post'])
def view_recipe_post():
    if session['lid'] != '':
        recipename=request.form['textfield']
        db = Database()
        qry = "SELECT * FROM recipe WHERE Recipe_name LIKE '%" +recipename+ "%'"
        res = db.select(qry)
        return render_template('admin/ViewRecipe.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/admin_delete_recipe/<id>')
def admin_delete_recipe(id):
    if session['lid'] != '':
        db=Database()
        qry="DELETE FROM `recipe` WHERE Recipe_id='"+id+"'"
        res=db.delete(qry)
        return'''<script>alert('Deleted succesfully');window.location='/view_recipe'</script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/edit_recipe/<id>')
def edit_recipe(id):
    if session['lid'] != '':
        db=Database()
        qry="SELECT * FROM recipe WHERE Recipe_id='"+id+"'"
        res=db.selectOne(qry)
        return render_template('admin/edit Recipe.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/edit_recipe_post',methods=['post'])
def edit_recipe_post():
    if session['lid'] != '':
        id=request.form['id']
        recipename = request.form['textfield']
        description = request.form['textarea']
        if 'fileField' in request.files:
            image = request.files['fileField']
            if image.filename!="":

                b = "IMG" + strftime("%Y%m%d%H%M%S") + "jpg"
                image.save("D:\\project\\New folder\\vegetablescanning\\static\\Recipe\\" + b)
                path = "/static/Recipe/" + b
                db = Database()
                qry = "UPDATE `recipe` SET Recipe_name='" + recipename + "',image='" + path + "', Description='" + description + "' WHERE Recipe_id='" + id + "'"
                res = db.update(qry)
                return '''<script>alert('Edited succesfully');window.location='/view_recipe'</script>'''
            else:
                db = Database()
                qry = "UPDATE `recipe` SET Recipe_name='" + recipename + "', Description='" + description + "' WHERE Recipe_id='" + id + "'"
                res = db.update(qry)
                return '''<script>alert('Edited succesfully');window.location='/view_recipe'</script>'''
        else:
            db = Database()
            qry = "UPDATE `recipe` SET Recipe_name='" + recipename + "', Description='" + description + "' WHERE Recipe_id='" + id + "'"
            res = db.update(qry)
            return '''<script>alert('Edited succesfully');window.location='/view_recipe'</script>'''


    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_review')
def view_review():
    if session['lid'] != '':
        db = Database()
        qry = "SELECT * FROM review INNER JOIN USER ON user.User_lid=review.User_lid INNER JOIN Store ON store.store_lid=review.Shop_lid"
        res = db.select(qry)
        return render_template('admin/viewreview.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_review_post',methods=['post'])
def view_review_post():
    if session['lid'] != '':
        db = Database()
        fromdate=request.form['textfield']
        todate=request.form['textfield2']
        qry = "SELECT * FROM review INNER JOIN USER ON user.User_lid=review.User_lid"
        res = db.select(qry)
        return render_template('admin/viewreview.html', data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_user')
def view_user():
    if session['lid'] != '':
        db=Database()
        qry="SELECT * FROM USER "
        res=db.select(qry)
        return render_template('admin/Viewuser.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/view_user_post',methods=['post'])
def view_user_post():
    if session['lid'] != '':
        username=request.form['textfield']
        db=Database()
        qry="SELECT * FROM user WHERE User_name LIKE '%"+username+"%'"
        res=db.select(qry)
        return render_template('admin/Viewuser.html', data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''



# @app.route('/view_review')
# def view_review():
#    db=Database()
#    qry="SELECT * FROM review INNER JOIN USER ON user.User_lid=review.User_lid INNER JOIN Store ON store.store_lid=review.Shop_lid "
#    res=db.select(qry)
#    return render_template('admin/viewreview.html',data=res)

@app.route('/shop_home')
def shop_home():
    if session['lid'] != '':
        return render_template('shop/index.html')
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/shopsignup')
def shopsignup():
    return render_template('shop/shop_index.html')

@app.route('/shopsignup_post',methods=['post'])
def shopsignup_post():
    db=Database()
    name=request.form['textfield11']
    place=request.form['textfield10']
    post=request.form['textfield9']
    pin=request.form['textfield8']
    phone=request.form['textfield7']
    licenseno=request.form['textfield6']
    photo=request.files['fileField']
    b = "IMG" + strftime("%Y%m%d%H%M%S") + "jpg"
    photo.save("D:\\project\\New folder\\vegetablescanning\\static\\store\\" + b)
    path = "/static/store/" + b
    email=request.form['textfield5']
    latitude=request.form['textfield4']
    longitude=request.form['textfield3']
    pswd=request.form['textfield2']
    cnfpswd=request.form['textfield']
    qry="INSERT INTO login (`Username`,`Password`,`Type`) VALUES('"+email+"','"+str(cnfpswd)+"','shop')"
    res=db.insert(qry)
    qry1="INSERT INTO `store`(`Store_lid`,`Store_name`,`Place`,`Post`,`Pin`,`Phone`,`Photo`,`Email`,`Latitude`,`Longitude`,`Status`,`Licencse_no`) VALUES ('"+str(res)+"','"+name+"','"+place+"','"+post+"','"+pin+"','"+phone+"','"+str(path)+"','"+email+"','"+latitude+"','"+longitude+"','pending','"+licenseno+"')"
    res1=db.insert(qry1)
    return '''<script>alert('Signup success');window.location='/'</script>'''

@app.route('/View_shop_profile')
def View_shop_profile():
    if session['lid'] != '':
        db=Database()
        qry="SELECT * FROM store WHERE Store_lid='"+str(session['lid'])+"'"
        res=db.selectOne(qry)

        return render_template('shop/viewshopprofile.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/Edit_profile')
def Edit_profile():
    if session['lid'] != '':
        db=Database()
        qry="SELECT * FROM store WHERE Store_lid='"+str(session['lid'])+"'"
        res=db.selectOne(qry)
        return render_template('shop/Editprofile.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/Edit_profile_post',methods=['post'])
def Edit_profile_post():
    if session['lid'] != '':
        db=Database()

        username=request.form['textfield']
        place=request.form['textfield2']
        post=request.form['textfield3']
        pin=request.form['textfield3']
        photo=request.files['fileField']
        b = "IMG" + strftime("%Y%m%d%H%M%S") + "jpg"
        photo.save("D:\\project\\New folder\\vegetablescanning\\static\\store\\" + b)
        path = "/static/store/" + b
        email=request.form['textfield5']
        latitude=request.form['textfield6']
        longitude=request.form['textfield7']
        if request.files!=None:
            if photo.filename!="":
                qry = "UPDATE `store` SET Store_name='" + username + "',Place='" + place + "',Post='" + post + "',Pin='" + pin + "',Photo='" + path + "',Email='" + email + "',Latitude='" + latitude + "',Longitude='" + longitude + "' WHERE Store_lid='"+str(session['lid'])+"'"
                res=db.update(qry)
            else:
                qry = "UPDATE `store` SET Store_name='" + username + "',Place='" + place + "',Post='" + post + "',Pin='" + pin + "',Email='" + email + "',Latitude='" + latitude + "',Longitude='" + longitude + "' WHERE Store_lid='" + str(
                    session['lid']) + "'"
                res = db.update(qry)
        else:
            qry = "UPDATE `store` SET Store_name='" + username + "',Place='" + place + "',Post='" + post + "',Pin='" + pin + "',Email='" + email + "',Latitude='" + latitude + "',Longitude='" + longitude + "' WHERE Store_lid='" + str(
                session['lid']) + "'"
            res = db.update(qry)
        return '''<script>alert('Edited Succesfully');window.location='/View_shop_profile'</script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/shop_add_item')
def shop_add_item():
    if session['lid'] != '':
        qry="SELECT * FROM `vegetables`"
        db=Database()
        res=db.select(qry)
        return render_template('shop/Additem.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/add_item_post',methods=['post'])
def add_item_post():
    if session['lid'] != '':
        vegname=request.form['select']
        quantity = request.form['textfield2']
        db=Database()
        qry="INSERT INTO item (Store_lid,Veg_id,Quantity)VALUES('"+str(session['lid'])+"','"+vegname+"','"+quantity+"')"
        res=db.update(qry)
        return '''<script>alert('Added Succesfully');window.location='/shop_add_item'</script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/Manage_items')
def Manage_items():
    if session['lid'] != '':
        db=Database()
        qry="SELECT * FROM `vegetables` INNER JOIN `item`ON `item`.`Veg_id`=`vegetables`.`Veg_id` WHERE `item`.`Store_lid`='"+str(session['lid'])+"'"
        res=db.select(qry)
        return render_template('shop/Manageitems.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''

@app.route('/shop_delete_item/<id>')
def shop_delete_item(id):
    if session['lid'] != '':
        db=Database()
        qry="DELETE FROM `item` WHERE Item_id='"+id+"'"
        res=db.delete(qry)
        return '''<script>alert('deleted successfully');window.location='/Manage_items'</Script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/shop_edit_item/<id>')
def shop_edit_item(id):
    if session['lid'] != '':
        db=Database()
        qry="SELECT * FROM `item` WHERE `Item_id`='"+id+"'"
        res=db.selectOne(qry)
        return render_template('shop/shop_edit_item.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/edit_item_post',methods=['post'])
def edit_item_post():
    if session['lid'] != '':
        id=request.form['id']
        Veg_name =request.form['textfield']
        Image =request.files['filefield']
        a = "IMG" + strftime("%Y%m%d%M%M%S") + "jpg"
        Image.save("C:\\Users\\chinnu\\PycharmProjects\\vegetablescanning\\ststic\\Vegetable\\" +a)
        path ="/static/Vegetables/" + a
        db=Database()

        return '''<script>alert('deleted successfully'); window.location='/Manage_items'</script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''





@app.route('/Send_complaint')
def Send_complaint():
    if session['lid'] != '':
        db=Database()
        return render_template('shop/Sendcomplaint.html')
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/Send_complaint_post',methods=['post'])
def Send_complaint_post():
    if session['lid'] != '':
        complaint=request.form['textarea']
        db=Database()
        qry="INSERT INTO complaint (`User_lid`,`Date`,`Complaint`,`Reply`,`Status`,`type`)VALUES('"+str(session['lid'])+"',curdate(),'"+complaint+"','pending','pending','shop')"
        res=db.insert(qry)
        return '''<script>alert('Sending successfully');window.location='/Send_complaint'</Script>'''
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_reply')
def view_reply():
    if session['lid'] != '':
        db=Database()
        qry="select * from complaint where User_lid='"+str(session['lid'])+"' "
        res=db.select(qry)
        return render_template('shop/viereply.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_reviewlv')
def view_reviewlv():
    if session['lid'] != '':
        db=Database()
        qry="SELECT `review`.*,`user`.`User_lid`,`user`.`User_name` FROM `review` INNER JOIN `user` ON `review`.`User_lid`=`user`.`User_lid` WHERE `review`.`Shop_lid`='"+str(session['lid'])+"'"
        res=db.select(qry)
        return render_template('shop/viewreviewlevel2.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/Search_review',methods=['post'])
def Search_review():
    if session['lid'] != '':
        from_Date=request.form['textfield']
        to_Date=request.form['textfield2']
        db=Database()
        qry = "SELECT `review`.*,`user`.`User_lid`,`user`.`User_name` FROM `review` INNER JOIN `user` ON `review`.`User_lid`=`user`.`User_lid` WHERE `review`.`Shop_lid`='" + str(session['lid']) + "' and Date between '"+from_Date+"' and '"+to_Date+"'"
        res = db.select(qry)
        return render_template('shop/viewreviewlevel2.html', data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/shop_additem')
def shop_additem():
    if session['lid'] != '':
        db=Database()
        qry="Select * from Vegetables"
        res=db.select(qry)
        return render_template('shop/Additem.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/shop_additem_post',methods=['post'])
def shop_additem_post():
    if session['lid'] != '':
        veg_id=request.form['select']
        qty=request.form['textfield2']
        db=Database()

        qry="SELECT * FROM `item` WHERE `Veg_id`='"+veg_id+"' AND `Store_lid`='"+str(session['lid'])+"'"
        res=db.selectOne(qry)
        if res is None:
            qry="INSERT INTO `item`(`Store_lid`,`Veg_id`,`Quantity`)  VALUES ('"+str(session['lid'])+"','"+veg_id+"','"+qty+"')"
            res=db.insert(qry)
            return "<script>alert('Added successfully');window.location='/shop_additem'</script>"
        else:
            qry="UPDATE `item` SET `Quantity`=`Quantity`+'"+ qty +"'   WHERE `Store_lid`='"+str(session['lid'])+"' AND `Veg_id`='"+veg_id+"'"
            print(qry)
            db.update(qry)
        return"<script>alert('Updated successfully'); window.location='/shop_additem'</script>"
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''


@app.route('/view_shop_item')
def view_shop_item():
    if session['lid'] != '':
        db=Database()
        qry="SELECT * FROM `item` INNER JOIN `vegetables` ON `vegetables`.`Veg_id`=`item`.`Veg_id` WHERE `item`.`Store_lid`='"+str(session['lid'])+"'"
        res=db.select(qry)
        return render_template('shop/view_stock.html',data=res)
    else:
        return '''<script>alert("You Are Logout....");window.location='/'</script>'''















#====================ANDROID========================


@app.route('/and_view_shopproduct',methods=['post'])
def and_view_shopproduct():
    db=Database()

    shoplid=request.form['shop_lid']
    print(shoplid)
    qry="SELECT * FROM `item` INNER JOIN `vegetables` ON `item`.`Veg_id`=`vegetables`.`Veg_id` WHERE `item`.`Store_lid`='"+shoplid+"'"
    res=db.select(qry)
    print(res)
    return jsonify(status='ok',users=res)



@app.route('/and_login_post', methods=['post'])
def and_login_post():
    username = request.form['username']
    password = request.form['password']
    db=Database()
    qry="select * from login where Username='"+ username+"' and Password='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:
        return jsonify(status='ok',lid=res['lid'],type=res['Type'])
    else:
         return jsonify(status='not')

@app.route('/and_user_signup',methods=['post'])
def and_user_signup():
    name=request.form['name']
    place=request.form['place']
    post=request.form['post']
    pin=request.form['pin']
    city=request.form['city']
    phone=request.form['phone']
    email=request.form['email']
    photo=request.form['Photo']
    cnfmpswd=request.form['cnfmpswd']
    import time, datetime

    import base64

    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(photo)
    fh = open("D:\\project\\New folder\\vegetablescanning\\static\\user\\" + timestr + ".jpg", "wb")
    path = "/static/user/" + timestr + ".jpg"
    fh.write(a)
    fh.close()

    db=Database()
    qry="INSERT INTO login (`Username`,`Password`,`Type`) VALUES('"+email+"','"+str(cnfmpswd)+"','user')"
    res=db.insert(qry)
    qry1="INSERT INTO`user`(User_lid,`User_name`,`Place`,`Post`,`Pin`,`City`,`Phone`,`Email`,`Photo`) VALUES ('"+str(res)+"','"+name+"','"+place+"','"+post+"','"+pin+"','"+city+"','"+phone+"','"+email+"','"+str(path)+"')"
    res=db.insert(qry1)
    return jsonify(status='ok')





@app.route('/and_user_viewprofile',methods=['post'])
def and_user_viewprofile():
    userlid=request.form['userlid']
    db=Database()
    qry="SELECT * FROM `user` WHERE `User_lid`='"+userlid+"'"
    res=db.selectOne(qry)
    return jsonify(status='ok',name=res['User_name'],place=res['Place'],post=res['Post'],pin=res['Pin'],city=res['City'],phone=res['Phone'],email=res['Email'],photo=res['Photo'])

@app.route('/and_user_editprofile',methods=['post'])
def and_user_editprofile():
    lid=request.form['lid']
    name = request.form['name']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    city = request.form['city']
    phone = request.form['phone']
    email = request.form['email']
    photo = request.form['Photo']


    import time, datetime

    import base64

    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(photo)
    fh = open("D:\\project\\New folder\\vegetablescanning\\static\\user\\" + timestr + ".jpg", "wb")
    path = "/static/user/" + timestr + ".jpg"
    fh.write(a)
    fh.close()



    db=Database()
    if(photo=="none"):

        qry = "UPDATE `user` SET `User_name`='" + name + "',`Place`='" + place + "',`Post`='" + post + "',`Pin`='" + pin + "',`City`='" + city + "',`Phone`='" + phone + "',`Email`='" + email + "' WHERE `User_lid`='" + lid + "'"
        res = db.update(qry)
        return jsonify(status='ok')
    else:
        qry = "UPDATE `user` SET `User_name`='" + name + "',`Place`='" + place + "',`Post`='" + post + "',`Pin`='" + pin + "',`City`='" + city + "',`Phone`='" + phone + "',`Email`='" + email + "',`Photo`='" + path + "' WHERE `User_lid`='" + lid + "'"
        res = db.update(qry)
        return jsonify(status='ok')

@app.route('/and_recipeinfo',methods=['post'])
def and_recipeinfo():
    lid=request.form['lid']
    db=Database()
    qry = "SELECT * FROM `recipe`"
    # qry="SELECT * FROM `item` INNER JOIN `store` ON `item`.`Store_lid`= `store`.`Store_lid` JOIN `vegetables` ON `vegetables`.`Veg_id`=`item`.`Veg_id`"
    res=db.select(qry)
    print(res)
    return jsonify(status='ok',data=res)

@app.route('/and_viewshop',methods=['post'])
def and_viewshop():
    db=Database()
    qry="SELECT * FROM store"
    res=db.select(qry)
    return jsonify(status='ok',users=res)


@app.route('/and_manage_review',methods=['post'])
def and_manage_review():
    lid = request.form['lid']
    l_id=request.form['shop_lid']
    review = request.form['review']
    rating = request.form['rating']

    db = Database()
    qry = "INSERT INTO `review`(`Shop_lid`,`User_lid`,`Review`,`Rating`,`Date`) VALUES ('"+l_id+"' ,'"+lid+"','"+review+"','"+rating+"',curdate())"
    res = db.insert(qry)
    return jsonify(status='ok')




@app.route('/and_sendcomplaintandreply',methods=['post'])

def and_sendcomplaintandreply():
    lid=request.form['lid']

    complaint=request.form['complaint']

    db=Database()
    qry="INSERT INTO `complaint`(`User_lid`,`Date`,`Complaint`,`Status`,`Reply`,`type`) VALUES('"+lid+"',curdate(),'"+complaint+"','pending','pending','user')"
    res=db.insert(qry)

    return jsonify(status='ok')

@app.route('/and_viewreply',methods=['post'])
def and_viewreply():
    lid=request.form['lid']
    db=Database()
    res=db.select("SELECT * FROM `complaint` WHERE `User_lid`='"+lid+"'")

    return jsonify(status='ok',data=res)






@app.route('/and_changepswd',methods=['post'])
def and_changepswd():
    lid=request.form['lid'];
    currentpswd=request.form['Password'];
    newpswd=request.form['npassword'];
    db=Database()
    qry1="SELECT * FROM `login` WHERE `lid`='"+lid+"' AND `Password`='"+currentpswd+"'"
    res=db.selectOne(qry1)
    if res is not None:
        qry2="UPDATE `login` SET `Password`='"++"' WHERE `lid`='"++"'"
        res=db.update(qry2)
        return jsonify(status="ok")
    else:
        return jsonify(status="no")


@app.route('/and_detect',methods=['post'])
def and_detect():
    photo=request.form['photo'];
    import time, datetime

    import base64

    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(photo)
    fh = open("D:\\project\\New folder\\vegetablescanning\\static\\detect\\" + timestr + ".jpg", "wb")
    path = "/static/detect/" + timestr + ".jpg"
    fh.write(a)
    fh.close()

    image_data = tf.gfile.FastGFile("D:\\project\\New folder\\vegetablescanning\\static\\detect\\" + timestr + ".jpg", 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("D:\\project\\New folder\\vegetablescanning\\logs\\output_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("D:\\project\\New folder\\vegetablescanning\\logs\\output_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    print(tf.summary)
    model_vars = tf.trainable_variables()
    slim.model_analyzer.analyze_vars(model_vars, print_info=True)


    items=[]

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                               {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        for node_id in top_k:
            human_string = label_lines[node_id]


            score = predictions[0][node_id]
            if score>0.4:

                items.append(human_string)
                print('%s (score = %.5f)' % (human_string, score))


    db=Database()
    qry="SELECT * FROM `recipe`"
    res=db.select(qry)

    fnl=[]
    for i in res:

        recpid=i['Recipe_id']
        recpname=i['Recipe_name']
        recpimg=i['Image']
        dscrption=i['Description']

       # print(recpname)


        qry1="SELECT * FROM `recipe_item` INNER JOIN `vegetables` ON `recipe_item`.`Veg_id`=`vegetables`.`Veg_id` where `Rec_id`='"+str(recpid)+"'"
        resa=db.select(qry1)
        s=[]
        for j in resa:
            vegid = j['Veg_id']
            vegname = j['Veg_name']

            s.append(vegname)

            #print("kgghjgh",vegname)


        c=0
        for m in s:
            if m in items:
                c=c+1

        #print(c)
        if c>0:
            fnl.append({'recpid':recpid,'recpname':recpname,'recpimg':recpimg,'dscrption':dscrption,'c':c})


    print(fnl)


    return jsonify(status="ok", data=fnl)








if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)

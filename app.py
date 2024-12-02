from flask import *
from flask_restful import Api
from flask_jwt_extended import JWTManager


app = Flask(__name__)

# set up jwt 
from datetime import timedelta
app.secret_key = "Remick"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=3)

jwt = JWTManager(app)

# make the app an api
api = Api(app)

# from view.views import MemberSignup,MembersSignin,memberprofile, AddDependants,ViewDependants,ViewLabTests,Bookings,ViewBooking, MakePayment, AdminSignup, AdminSignin, AdminProfile, AddNurse, ViewNurse, NurseProfile,resetpassword,resetmemberpassword,adminpassword
# api.add_resource(MemberSignup, "/api/member_signup")
# api.add_resource(MembersSignin, "/api/member_signin")
# api.add_resource(memberprofile, "/api/member_profile")
# api.add_resource(AddDependants,"/api/add_dependants")
# api.add_resource(ViewDependants,"/api/view_dependants")
# api.add_resource(ViewLabTests,"/api/viewlab_test")
# api.add_resource(Bookings,"/api/bookings")
# api.add_resource(ViewBooking,"/api/viewbookings")
# api.add_resource(MakePayment,"/api/make_payment")
# api.add_resource(AdminSignup,"/api/admin_signup")
# api.add_resource(AdminSignin,"/api/admin_signin")
# api.add_resource(AdminProfile,"/api/admin_profile")
# api.add_resource(AddNurse,"/api/add_nurse")
# api.add_resource(ViewNurse,"/api/view_nurse")
# api.add_resource(NurseProfile,"/api/nurse_profile")

# api.add_resource(resetpassword,"/api/reset_password")
# api.add_resource(resetmemberpassword,"/api/member_password")
# api.add_resource(adminpassword,"/api/admin_password")


if __name__ =='__main__':
    app.run(debug=True)
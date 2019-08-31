function validateEmail(email) {
        var re = /\S+@\S+\.\S+/;
        return re.test(email);
    }
function kiemtra(){
            sessionStorage.tenhocvien = $("input[name='tenhocvien']").val();
            sessionStorage.sdthocvien = $("input[name='sdthocvien']").val();
      var phoneno = /^([a-zA-Z0-9_-]){8,11}$/;
    var phoneval = $("input[name='sdthocvien']").val();
            var name = sessionStorage.tenhocvien;
            var tel = sessionStorage.sdthocvien;
            var email = $("input[name='emailhocvien']").val();
      if($("input[name='tenhocvien']").val() == "")
        {
            alert("Vui lòng nhập Họ tên!");
        }
        else if($("input[name='emailhocvien']").val()=="" || !validateEmail($("input[name='emailhocvien']").val())){
            alert("Email phải hợp lệ !");
            return false;
        }
        else if((!phoneval.match(phoneno)) ){
            alert("Số điện thoại bạn điền không hợp lệ !");
            return false;
        }
        }

package com.nitin.myapplication.Class;

public class Customer {
       private String first_name;
       private String last_name;
       private String phone;
       private String email;
       private String address;
       private String blacklist;
    public Customer(String first_name,String last_name,String email,String phone,String address,String blacklist){
        setAddress(address);
        setBlacklist(blacklist);
        setEmail(email);
        setPhone(phone);
        setFirst_name(first_name);
        setLast_name(last_name);
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setBlacklist(String blacklist) {
        this.blacklist = blacklist;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getEmail() {
        return email;
    }

    public String getPhone() {
        return phone;
    }

    public String getLast_name() {
        return last_name;
    }

    public String getFirst_name() {
        return first_name;
    }

    public String getBlacklist() {
        return blacklist;
    }

    public String getAddress() {
        return address;
    }

}


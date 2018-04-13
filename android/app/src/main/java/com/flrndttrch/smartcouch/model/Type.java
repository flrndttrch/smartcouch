package com.flrndttrch.smartcouch.model;

import com.google.gson.annotations.SerializedName;

public class Type {
    @SerializedName("name")
    private String name;

    public Type(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

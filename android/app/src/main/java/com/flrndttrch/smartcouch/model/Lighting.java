package com.flrndttrch.smartcouch.model;

import com.google.gson.annotations.SerializedName;

public class Lighting {
    @SerializedName("id")
    private int id;
    @SerializedName("active")
    private boolean active;
    @SerializedName("brightness")
    private float brightness;
    @SerializedName("color_r")
    private int colorR;
    @SerializedName("color_g")
    private int colorG;
    @SerializedName("color_b")
    private int colorB;
    @SerializedName("color_name")
    private String colorName;
    @SerializedName("creation_date")
    private String creationDate;
    @SerializedName("description")
    private String description;
    @SerializedName("type")
    private Type type;
    @SerializedName("user")
    private User user;

    public Lighting(float brightness, int colorR, int colorG, int colorB, String colorName,
                    String description, Type type, User user) {
        this.brightness = brightness;
        this.colorR = colorR;
        this.colorG = colorG;
        this.colorB = colorB;
        this.colorName = colorName;
        this.description = description;
        this.type = type;
        this.user = user;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public float getBrightness() {
        return brightness;
    }

    public void setBrightness(float brightness) {
        this.brightness = brightness;
    }

    public int getColorR() {
        return colorR;
    }

    public void setColorR(int colorR) {
        this.colorR = colorR;
    }

    public int getColorG() {
        return colorG;
    }

    public void setColorG(int colorG) {
        this.colorG = colorG;
    }

    public int getColorB() {
        return colorB;
    }

    public void setColorB(int colorB) {
        this.colorB = colorB;
    }

    public String getColorName() {
        return colorName;
    }

    public void setColorName(String colorName) {
        this.colorName = colorName;
    }

    public String getCreationDate() {
        return creationDate;
    }

    public void setCreationDate(String creationDate) {
        this.creationDate = creationDate;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
}

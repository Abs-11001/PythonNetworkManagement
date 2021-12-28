var file = document.getElementById("file");
var des = document.querySelector("#des");
var rename = document.querySelector("#rename");
var h2 = document.querySelector(".change_color");
var idx = 0;
var interval = 400;
var text = "你无权访问！！！";
function change()
{
    
    h2.innerHTML = text.substring(idx, text.length) + text.substring(0, idx);
    var x = Math.floor(Math.random() * (256 - 0)) + 0;
    var y = Math.floor(Math.random() * (256 - 0)) + 0;
    var z = Math.floor(Math.random() * (256 - 0)) + 0;
    h2.style.color = "rgb" + "(" + x +"," + y + "," + z + ")";
    idx ++;
    if(idx == text.length)
    {
        idx = 0;
    }
    window.setTimeout("change()",interval);
}
des.onfocus = function()
{
    if(des.value == "请输入文件的描述...")
    {
        des.value = "";
    }
    des.style.color = "black";
}
des.onblur = function()
{
    if(des.value == "")
    {
        des.value = "请输入文件的描述...";
        des.style.color = "#999999";
    }
}
rename.onfocus = function()
{
    if(rename.value == "重命名...")
    {
        rename.value = "";
    }
    rename.style.color = "black";
}
rename.onblur = function()
{
    if(rename.value == "")
    {
        rename.value = "重命名...";
        rename.style.color = "#999999";
    }
}

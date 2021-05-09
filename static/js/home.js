let users;
$.ajax({ 
	type: 'GET',
    url: 'http://127.0.0.1:5000/users', 
    success: function(response){ 
        co=0;
        users=response;
        response.forEach(function(data){
            let carddata=`<div class="card"><div class="blurring dimmable image"><img src="${data.img}"></div><div class="content" align="center">`+
                         `<p class="header">${data.name}</p><div class="meta"><span class="date">${data.dob}</span></div></div>`+
                         `<div class="extra content"><a onclick=showdetails(${co})>View details</a></div></div>`;
            $('#users').append(carddata);
            co+=1;
        });
    },
    error: function(response){
        console.log(response);
    }
});

function showdetails(val){
    let data=users[val]
    let model=`<p class="close icon">X</p>
                <div class="header">
                ${data.name}
                </div>
                <div class="image content">
                <div class="ui medium image">
                    <img src="${data.img}">
                </div>
                <div class="description">
                    <div class="ui header">Details</div>
                    <p>Firstname: ${data.firstname}</p>
                    <p>Lastname: ${data.lastname}</p>
                    <p>Email: ${data.email}</p>
                    <p>DOB: ${data.dob}</p>
                    <p>Age: ${data.age}</p>
                    <p>Address: ${data.more.address}</p>
                    <p>District: ${data.more.district}</p>
                    <p>Pincode: ${data.more.pincode}</p>
                </div>
                </div>
                <div class="actions">
                <div class="ui black deny button">
                <p onclick=prev("${val}")>Prev</p>
                </div>
                <div class="ui positive right button">
                <p onclick=next("${val}")>Next</p>
                </div>
            </div>
         `
    $('.modal').html(model);
    $('.ui.modal').modal('show')
}

function next(val){
    val=Number(val);
    val+=1;
    console.log(val);
    if(val<users.length){
        showdetails(val);
    }
    console.log("kise");
}

function prev(val){
    val=Number(val);
    val-=1;
    console.log(val);
    if(val>=0){
        showdetails(val);
    }
    console.log("kise");
}
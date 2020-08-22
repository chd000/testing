(function ($) {
    $(document).on("click", "#sendAnsButton", function () {
        $.ajax({
            type: "GET",
            url: 'http://127.0.0.1:8000/result',
            data: {
                list: resultList()
            },
            dataType: 'json',
            success: function () {
            }
        })
        alert('Ваши ответы отправлены, нажмите "Завершить тест"')
    })
})(jQuery);

/*
 $(document).ready(function () {
     $("#myselect option").on('change', function () {
         $.cookie('myCookie', $("#myselect option").val());
     });

     let cookieValue = $.cookie('myCookie');
     if (typeof cookieValue !== "undefined") {
         $("#myselect option").val(cookieValue);
     }
 });


$("input.checkbox").each(function () {
    let mycookie = $.cookie($(this).attr('id'));
    if (mycookie && mycookie === "true") {
        $(this).prop('checked', mycookie);
    }
});


$("input.checkbox").change(function () {
    $.cookie($(this).attr('id'), $(this).prop('checked'), {
        path: '/',
        expires: 365,
    });
});
*/

//$("#myselect option").each(function () {
//    console.log(this.id + ' ' + this.text + ' ' + this.value);
//});

function getSequence() {
    let selectors = document.getElementsByClassName('myselect')
    let list = []
    //$("#myselect option").each(function () {
    //   if ($(this).is(':selected')) {
    //    $(this).remove();
    // }
    //});
    for (let index = 0; index < selectors.length; index++) {
        list.push(selectors[index].value)
    }
    return list;
}

function getCheckedCheckBoxes() {
    let checkboxes = document.getElementsByClassName('checkbox');
    let checkboxesChecked = [];
    let buttonsArray = []
    let checkboxesIdArray = []
    for (let j = 0; j < 20; j++) {
        let thisButton = document.getElementById(j)
        thisButton.style.backgroundColor = '#e6e6e6';
        buttonsArray.push(thisButton)
    }
    for (let index = 0; index < checkboxes.length; index++) {
        if (checkboxes[index].checked) {
            // buttonsArray[index].style.backgroundColor = '#a6a6a6';
            checkboxesChecked.push(checkboxes[index].value);
        }
    }
    return checkboxesChecked;
}

function resultList() {
    let allAnswersList = [];
    allAnswersList = getCheckedCheckBoxes().concat(getSequence())
    return allAnswersList
}

function changeColorIfAns(type) {
    if (type === 1) {
        let selected = document.getElementsByClassName('myselect')
    }
    if (type === 2) {
        let checkboxes = document.getElementsByClassName('checkbox')
        for (let index = 0; index < checkboxes.length; index++) {
            if (checkboxes[index].checked) {

            }
        }
    }
}

function scrollToQuestion(obj) {
    let thisId = obj.id
    document.getElementById('questionArea' + thisId).scrollIntoView({behavior: "smooth", block: "center"});
}
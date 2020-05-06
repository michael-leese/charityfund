 function sendEmail(contactForm){
    var serviceId = "gmail";
    var templateId = "charity_fund";
    emailjs.send(serviceId, templateId, {
      org: contactForm.orgEmail.value,
      appeal: contactForm.appealEmail.value,
      content: contactForm.contentEmail.value,
      to_email: contactForm.toEmail.value,
      from_name: contactForm.nameEmail.value,
      from_email: contactForm.fromName.value
  }).then(function(response) {
       alert('SUCCESS!', response);
       $('#submitEmail').hide();
       $('#contentEmail').empty();
    }, function(error) {
       alert('FAILED! Please try later.', error);
    });
 }

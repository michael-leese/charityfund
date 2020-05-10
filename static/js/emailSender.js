 function sendEmail(contactForm){
   var serviceId = "gmail";
   var templateId = "charity_fund";
   emailjs.send(serviceId, templateId, {
     org: contactForm.orgEmail.value,
     appeal: contactForm.appealEmail.value,
     content: contactForm.contentEmail.value,
     to_email: contactForm.toEmail.value,
     from_name: contactForm.fromName.value,
     from_email: contactForm.fromEmail.value
 }).then(function(response) {
      alert('SUCCESS!', response.status);
   }, function(error) {
      alert('FAILED! Please try later.', error);
   });
}
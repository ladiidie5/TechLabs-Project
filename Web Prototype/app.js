
// Nav bar configuration

    //Smooth scroll to team members. 
var teamBtn = document.getElementById("teamBtn");

teamBtn.addEventListener("click", scrollToTeam);

function scrollToTeam() {
    var teamTitle = document.getElementById("teamTitle"); 
    teamTitle.scrollIntoView({
        behaviour: 'smooth',
    });
  };

  
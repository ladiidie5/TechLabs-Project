
// Nav bar configuration

    //Smooth scroll to team members. Not working for whatever reason I can't understand. 
const teamBtn = document.getElementById("teamBtn");

teamBtn.addEventListener("click", scrollToTeam);

function scrollToTeam() {
    const teamTitle = document.getElementById("teamTitle"); 
    teamTitle.scrollIntoView({behavior: 'smooth', block: 'nearest', inline: 'start' });
  };



  
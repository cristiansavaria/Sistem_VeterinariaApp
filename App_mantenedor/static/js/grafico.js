




  const labels = [
    'Enero',
    'February',
    'March',
    'April',
    'May',
    'June',
  ];

  const dataLine = {
    labels: labels,
    datasets: [{
      label: 'Atenciones 2022',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [0, 10, 5, 2, 20, 30, 45],
    }]
  };

  const config = {
    type: 'line',
    data: dataLine,
    options: {}
  };



  const myChart = new Chart(
    document.getElementById('myChart'),
    config
  );





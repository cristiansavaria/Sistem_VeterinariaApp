

  console.log('hola')


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



  const data = {
    labels: [
      'Red',
      'Green',
      'Yellow',
      'Grey',
      'Blue'
    ],
    datasets: [{
      label: 'My First Dataset',
      data: [11, 16, 7, 3, 14],
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(75, 192, 192)',
        'rgb(255, 205, 86)',
        'rgb(201, 203, 207)',
        'rgb(54, 162, 235)'
      ]
    }]
  };
  // </block:setup>
  
  // <block:config:0>
  const configs = {
    type: 'polarArea',
    data: data,
    options: {}
  };
  // </block:config>
  
  const myCharts = new Chart(
    document.getElementById('myCharts'),
    configs
  );

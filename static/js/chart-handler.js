// === Parseo de datos desde Flask ===
const fechasPeso = pesos.map(p => new Date(p.fecha).toLocaleDateString());
const valoresPeso = pesos.map(p => p.peso);

const caloriasPorFecha = {};
alimentos.forEach(alimento => {
  const fecha = new Date(alimento.fecha).toLocaleDateString();
  caloriasPorFecha[fecha] = (caloriasPorFecha[fecha] || 0) + alimento.calorias;
});

const fechasCalorias = Object.keys(caloriasPorFecha);
const valoresCalorias = Object.values(caloriasPorFecha);

// === Configuración común para ambos gráficos ===
const chartDefaults = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      labels: {
        color: '#2c3e50',
        font: {
          size: 14,
          weight: 'bold'
        }
      }
    },
    tooltip: {
      backgroundColor: '#34495e',
      titleColor: '#ecf0f1',
      bodyColor: '#ecf0f1',
      padding: 10,
      cornerRadius: 6
    }
  },
  scales: {
    x: {
      ticks: {
        color: '#2c3e50',
        font: {
          size: 12
        }
      },
      grid: {
        display: false
      }
    },
    y: {
      beginAtZero: true,
      ticks: {
        color: '#2c3e50',
        font: {
          size: 12
        }
      },
      grid: {
        color: '#ecf0f1'
      }
    }
  }
};

// === Gráfico de Peso ===
const pesoChart = new Chart(document.getElementById('pesoChart'), {
  type: 'line',
  data: {
    labels: fechasPeso,
    datasets: [{
      label: 'Peso (kg)',
      data: valoresPeso,
      borderColor: '#2980b9',
      backgroundColor: 'rgba(41, 128, 185, 0.2)',
      pointBackgroundColor: '#2980b9',
      pointRadius: 4,
      pointHoverRadius: 6,
      fill: true,
      tension: 0.4
    }]
  },
  options: {
    ...chartDefaults,
    scales: {
      ...chartDefaults.scales,
      y: {
        ...chartDefaults.scales.y,
        beginAtZero: false,
        suggestedMin: Math.min(...valoresPeso) - 2,
        suggestedMax: Math.max(...valoresPeso) + 2
      }
    }
  }
});

// === Gráfico de Calorías ===
const caloriasChart = new Chart(document.getElementById('caloriasChart'), {
  type: 'bar',
  data: {
    labels: fechasCalorias,
    datasets: [{
      label: 'Calorías consumidas',
      data: valoresCalorias,
      backgroundColor: '#e67e22',
      borderRadius: 6,
      hoverBackgroundColor: '#d35400'
    }]
  },
  options: chartDefaults
});

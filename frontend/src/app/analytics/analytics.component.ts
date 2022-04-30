import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Chart, registerables } from 'chart.js';
import { DataService } from '../services/data.service';

Chart.register(...registerables);

@Component({
  selector: 'app-analytics',
  templateUrl: './analytics.component.html',
  styleUrls: ['./analytics.component.css'],
})
export class AnalyticsComponent implements OnInit {
  @ViewChild('chart', { static: true }) chart!: ElementRef;
  myChart: any;
  region = '';
  data: any = [];
  ctx: any = null;
  loading = false;
  constructor(private dataService: DataService) {}

  ngOnInit(): void {
    this.initChart();
    this.loadData();
  }
  
  loadData() {
    this.loading = true;
    this.dataService.getChartDataByRegion(this.region).subscribe((data) => {
      this.data = data;
      this.setChartData();
      this.loading = false;
    });
  }

  initChart() {
    const ctx = this.chart.nativeElement.getContext('2d');
    this.myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: this.data.map((item: any) => item.label),
        datasets: [
          {
            label: '# of Policies by month',
            data: [],
            backgroundColor: [],
            borderColor: [],
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  }

  onRegionChange(region: any) {
    this.region = region.target.value;
    this.loadData();
  }

  setChartData() {
    // const ctx = this.chart.nativeElement.getContext('2d');
    const colors = this.getNRandomColors(this.data.length);
    this.myChart.data.labels = this.data.map((item: any) => item.label);
    this.myChart.data.datasets[0].data = this.data.map((item: any) => item.value);
    this.myChart.data.datasets[0].backgroundColor = colors.map((item: any) => item.backgroundColor);
    this.myChart.data.datasets[0].borderColor = colors.map((item: any) => item.borderColor);
    this.myChart.update();
    // this.myChart = new Chart(ctx, {
    //   type: 'bar',
    //   data: {
    //     labels: this.data.map((item: any) => item.label),
    //     datasets: [
    //       {
    //         label: '# of Policies by month',
    //         data: this.data.map((item: any) => parseInt(item.value)),
    //         backgroundColor: colors.map((item: any) => item.backgroundColor),
    //         borderColor: colors.map((item: any) => item.borderColor),
    //         borderWidth: 1,
    //       },
    //     ],
    //   },
    //   options: {
    //     scales: {
    //       y: {
    //         beginAtZero: true,
    //       },
    //     },
    //   },
    // });
  }

  getNRandomColors(n: number) {
    const colors = [];
    for (let i = 0; i < n; i++) {
      colors.push(this.getRandomColorWithHalfOpacity());
    }
    return colors;
  }

  getRandomColorWithHalfOpacity() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return {
      backgroundColor: color + '50',
      borderColor: color + '80',
    };
  }
}

import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-list-policies',
  templateUrl: './list-policies.component.html',
  styleUrls: ['./list-policies.component.css'],
})
export class ListPoliciesComponent implements OnInit {
  pageNum = 1;
  pageSize = 10;
  policies: any[] = [];
  loading = true;
  loadingArr = new Array(10);
  pageData: any = {};
  query = '';

  policiesHeader = [
    {
      key: 'policy_id',
      label: 'Policy ID',
    },
    {
      key: 'date_of_purchase',
      label: 'Date of Purchase',
    },
    {
      key: 'customer_id',
      label: 'Customer ID',
    },
    {
      key: 'fuel',
      label: 'Fuel',
    },
    {
      key: 'vehicle_segment',
      label: 'Vehicle Segment',
    },
    {
      key: 'premium',
      label: 'Premium',
    },
    {
      key: 'bodily_injury_liability',
      label: 'bodily injury liability',
    },
    {
      key: 'personal_injury_protection',
      label: 'personal injury protection',
    },
    {
      key: 'property_damage_liability',
      label: 'property damage liability',
    },
    {
      key: 'collision',
      label: 'collision',
    },
    {
      key: 'comprehensive',
      label: 'comprehensive',
    },
    {
      key: 'gender',
      label: 'Gender',
    },
    {
      key: 'income_group',
      label: 'Income Group',
    },
    {
      key: 'region',
      label: 'Region',
    },
    {
      key: 'Customer_Marital_status',
      label: 'marital_status',
    },
  ];
  constructor(private dataService: DataService) {}

  ngOnInit(): void {
    this.loadData();
  }

  onPageChange(pageNum: number) {
    if (pageNum < 1 || pageNum > this.pageData.totalPages) return;
    this.pageNum = pageNum;
    this.loadData();
  }

  search() {
    this.pageNum = 1;
    this.loadData();
  }

  clear() {
    this.query = '';
    this.pageNum = 1;
    this.loadData();
  }

  async loadData() {
    this.loading = true;
    this.dataService
      .getPageData(this.pageNum, this.pageSize, this.query)
      .subscribe((data: any) => {
        this.policies = data.results.map((item: any) => ({
          doc_id: item.id,
          date_of_purchase: item.date_of_purchase,
          policy_id: item.policy.id,
          customer_id: item.customer.id,
          ...item.customer,
          ...item.policy
        }));

        this.pageData = {
          current: data.current,
          pageSize: data.page_size,
          total: data.count,
          totalPages: data.total_page,
        };
        this.loading = false;
      });
  }

  pagesToShow() {
    if ((this, this.pageData.totalPages <= 3)) {
      return new Array(this.pageData.totalPages);
    } else {
      const pages = new Array(3);
      if (this.pageNum == 1) {
        pages[0] = 1;
        pages[1] = 2;
        pages[2] = 3;
      } else if (this.pageNum == this.pageData.totalPages) {
        pages[0] = this.pageData.totalPages - 2;
        pages[1] = this.pageData.totalPages - 1;
        pages[2] = this.pageData.totalPages;
      } else {
        pages[0] = this.pageData.current - 1;
        pages[1] = this.pageData.current;
        pages[2] = this.pageData.current + 1;
      }
      return pages;
    }
  }
}

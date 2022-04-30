import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { data } from './data';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  private data: any[] = data;
  API = 'http://35.232.206.179/api/policy/customer_policies/';
  POLICY_API = 'http://35.232.206.179/api/policy/';
  CUSTOMER_API = 'http://35.232.206.179/api/customer/';
  CHART_API = 'http://35.232.206.179/api/policy/get_policy_by_month/';

  constructor(private http: HttpClient) {}

  getPageData(page: number, pageSize: number, searchTerm: string) {
    return this.http.get(
      this.API +
        '?page=' +
        page +
        '&page_size=' +
        pageSize +
        '&query=' +
        searchTerm
    );
  }

  getCustomerPolicies(id: string) {
    return this.http.get(this.API + id);
  }

  getChartDataByRegion(region: string) {
    return this.http.get(`${this.CHART_API}?region=${region}`);
  }

  putPolicy(id: string, policy: any) {
    return this.http.put(this.POLICY_API + id + '/', policy);
  }

  putCustomer(id: string, customer: any) {
    return this.http.put(this.CUSTOMER_API + id + '/', customer);
  }
}

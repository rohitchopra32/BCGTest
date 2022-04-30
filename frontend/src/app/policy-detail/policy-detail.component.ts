import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { forkJoin, zip } from 'rxjs';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-policy-detail',
  templateUrl: './policy-detail.component.html',
  styleUrls: ['./policy-detail.component.css'],
})
export class PolicyDetailComponent implements OnInit {
  id = '';
  data: any = null;
  policy: any = null;
  customer: any = null;
  loading = false;
  constructor(
    private route: ActivatedRoute,
    private dataService: DataService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.loadData();
  }

  loadData() {
    this.loading = true;
    this.cdr.detectChanges();
    this.id = this.route.snapshot.paramMap.get('id')!;
    this.dataService.getCustomerPolicies(this.id).subscribe((data: any) => {
      this.policy = JSON.parse(JSON.stringify(data.policy));
      this.customer = JSON.parse(JSON.stringify(data.customer));
      this.data = data;
      this.loading = false;
    });
  }

  async save() {
    this.loading = true;
    zip(
      this.dataService.putPolicy(this.policy.id, this.policy),
      this.dataService.putCustomer(this.customer.id, this.customer)
    ).subscribe({
      next: (...data) => {
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        alert('Error saving data');
        this.loading = false;
      }
    })
  }
}

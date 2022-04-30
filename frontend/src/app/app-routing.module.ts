import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AnalyticsComponent } from './analytics/analytics.component';
import { ListPoliciesComponent } from './list-policies/list-policies.component';
import { PolicyDetailComponent } from './policy-detail/policy-detail.component';

const routes: Routes = [
  {
    path: '',
    component: ListPoliciesComponent,
  },
  {
    path: 'policy/:id',
    component: PolicyDetailComponent
  },
  {
    path: 'analytics',
    component: AnalyticsComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}

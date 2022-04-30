import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ListPoliciesComponent } from './list-policies/list-policies.component';
import { PolicyDetailComponent } from './policy-detail/policy-detail.component';
import { HttpClientModule } from '@angular/common/http';
import { AnalyticsComponent } from './analytics/analytics.component';

@NgModule({
  declarations: [AppComponent, ListPoliciesComponent, PolicyDetailComponent, AnalyticsComponent],
  imports: [BrowserModule, AppRoutingModule, FormsModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}

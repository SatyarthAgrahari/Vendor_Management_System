from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


class Vendor(models.Model):
    # vendor information
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20,unique=True)

    # Performance Matrics
    on_time_delivery_rate =models.FloatField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    quality_rating_avg = models.FloatField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    average_response_time = models.FloatField(default=0, validators=[MinValueValidator(0)])
    fulfillment_rate = models.FloatField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    

    def __str__(self):
        return self.name
    
class PurchaseOrder(models.Model):
    # Purchase Order details
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20)

    # vandor rating and acknowledgement

    quality_rating = models.FloatField(null=True,blank=True, validators=[MinValueValidator(0),MaxValueValidator(5)])
    issue_date = models.DateTimeField(null=True,blank=True)
    acknowledgement_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.po_number
    

    def Update_performance_metrics(self):
        # Update vendor's performance metrics when the purchase order status changes

        # Update On-Time Delivery Rate if the order is completed and has a delivery date
        if self.status.lower() == "completed" and self.delivery_date is not None:
            self.vendor.on_time_delivery_rate = self.calculate_on_time_delivery_rate()

        # Update Quality Rating Average if the order is completed and has a quality rating
        if self.status.lower() == "completed" and self.quality_rating is not None:
            self.vendor.quality_rating_avg = self.calculate_quality_rating_avg()

         # Update Average Response Time if the acknowledgment date is not null
        if self.acknowledgement_date is not None:
            self.vendor.average_response_time = self.calculate_average_response_time()

        # Update Fulfillment Rate
        self.vendor.fulfillment_rate =self.calculate_fulfillment_rate()

        # Save the updated vendor instance
        self.vendor.save()

        def calculate_on_time_delivery_rate(self):
            # Fetch all completed purchase orders for the specific vendor
            completed_pos = PurchaseOrder.objects.filter(vendor=self.vendor, status= "completed")

            # Filter on-time deliveries based on the delivery date and acknowledgment date
            on_time_deliveries = completed_pos.filter(delivery_date__lte=models.F('acknowledgement_date'))

            # Calculate the on-time delivery rate as a percentage
            return (on_time_deliveries.count()/completed_pos.count())*100 if completed_pos.count()>0 else 0
        
        def calculate_quality_rating_avg(self):

            # Fetch all completed purchase orders for the specific vendor with a quality rating
            completed_pos = PurchaseOrder.objects.filter(vendor=self.vendor, status= "completed", calculate_quality__isnull=False)

            # Calculate the average quality rating
            return completed_pos.aggregate(models.Avg('quality_rating'))['quality_rating__avg'] or 0
        
        def calculate_average_response_time(self):

            # Fetch all completed purchase orders for the specific vendor with an acknowledgment date
            completed_pos = PurchaseOrder.objects.filter(vendor=self.vendor, acknowledgement_date__isnull=False)

            # Calculate the time difference between acknowledgment date and issue date for each completed purchase order
            response_times = [(po.acknowledgement_date - po.issue_date).total_seconds() for po in completed_pos] 

            # Compute the average response time
            return sum(response_times) / len(completed_pos) if completed_pos.exists() else 0
        
        def calculate_fulfillment_rate(self):

            # Fetch all completed purchase orders for the specific vendor
            completed_pos = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed')

            # Filter successfully fulfilled purchase orders (status 'completed' without issues)
            successful_fulfillments = completed_pos.objects.filter(issue_date__isnull=True)

            # Calculate the fulfillment rate as the percentage of successful fulfillments out of all completed purchase orders
            return (successful_fulfillments.count() / completed_pos.count()) * 100 if completed_pos.count() > 0 else 0
        
class HistoricalPerformance(models.Model):
    # Historical performance records
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    
    # Historical performance metrics
    on_time_delivery_rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    quality_rating_avg = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    average_response_time = models.FloatField(default=0, validators=[MinValueValidator(0)])
    fulfillment_rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"











#import "SWGCategoryManagedObjectBuilder.h"

/**
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/

@implementation SWGCategoryManagedObjectBuilder

-(instancetype)init {
    self = [super init];
    if (self != nil) {
    }
    return self;
}

-(SWGCategoryManagedObject*)createNewSWGCategoryManagedObjectInContext:(NSManagedObjectContext*)context {
    SWGCategoryManagedObject *managedObject = [NSEntityDescription insertNewObjectForEntityForName:NSStringFromClass([SWGCategoryManagedObject class]) inManagedObjectContext:context];
    return managedObject;
}

-(SWGCategoryManagedObject*)SWGCategoryManagedObjectFromSWGCategory:(SWGCategory*)object context:(NSManagedObjectContext*)context {
    SWGCategoryManagedObject* newSWGCategory = [self createNewSWGCategoryManagedObjectInContext:context];
    [self updateSWGCategoryManagedObject:newSWGCategory withSWGCategory:object];
    return newSWGCategory;
}

-(void)updateSWGCategoryManagedObject:(SWGCategoryManagedObject*)managedObject withSWGCategory:(SWGCategory*)object {
    if(!managedObject || !object) {
        return;
    }
    NSManagedObjectContext* context = managedObject.managedObjectContext;
    managedObject._id = [object._id copy];
    managedObject.name = [object.name copy];

}

-(SWGCategory*)SWGCategoryFromSWGCategoryManagedObject:(SWGCategoryManagedObject*)obj {
    if(!obj) {
        return nil;
    }
    SWGCategory* newSWGCategory = [[SWGCategory alloc] init];
    [self updateSWGCategory:newSWGCategory withSWGCategoryManagedObject:obj];
    return newSWGCategory;
}

-(void)updateSWGCategory:(SWGCategory*)newSWGCategory withSWGCategoryManagedObject:(SWGCategoryManagedObject*)obj {
    newSWGCategory._id = [obj._id copy];
    newSWGCategory.name = [obj.name copy];
}

@end

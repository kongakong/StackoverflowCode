//
//  TKWLUICollectionView.m
//  TestKBWithLabel
//
//  Created by Anthony Kong on 8/03/2014.
//  Copyright (c) 2014 Anthony Kong. All rights reserved.
//

#import "TKWLUICollectionView.h"
#import "TKWLUICollectionViewCell.h"

@implementation TKWLUICollectionView



- (NSInteger)numberOfSectionsInCollectionView:(UICollectionView *)collectionView {
    return 1;
}

- (NSInteger)collectionView:(UICollectionView *)collectionView numberOfItemsInSection:(NSInteger)section
{
    
    return 5;
}

- (UICollectionViewCell *)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath{
    static NSString *CellIdentifier = @"Cell";
    
    TKWLUICollectionViewCell *cell = [collectionView dequeueReusableCellWithReuseIdentifier:CellIdentifier
                                                                               forIndexPath:indexPath];

    // Look like we do not need it?
    //    if (cell == nil) {
    //        cell = [[TKWLUICollectionViewCell alloc] initWithFrame:
    //    }
    //
    
    UITextField *tf = [[UITextField alloc] initWithFrame:[cell bounds]];
    [tf setKeyboardType:UIKeyboardTypeNumberPad];
    [cell.lblTest addSubview:tf];
    [cell.lblTest setUserInteractionEnabled:YES];
    
    [cell.lblTest setText:[NSString stringWithFormat:@"cell %d", indexPath.row]];
    
    return cell;
    
}

@end
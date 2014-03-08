//
//  TKWLCell.m
//  TestKBWithLabel
//
//  Created by Anthony Kong on 8/03/2014.
//  Copyright (c) 2014 Anthony Kong. All rights reserved.
//

#import "TKWLCell.h"

@implementation TKWLCell


-(void) handleSingleTap:(UIGestureRecognizer *)gestureRecognizer  {
    NSLog(@"handleSingleTap called");
    
}

- (id)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier
{
    self = [super initWithStyle:style reuseIdentifier:reuseIdentifier];
    if (self) {
        // Initialization code
//        UITextField *tf = [[UITextField alloc] initWithFrame:CGRectMake(0, 0, 0, 0)];
//        [tf setKeyboardType:UIKeyboardTypeNumberPad];
//        [self.lblTest addSubview:tf];
//        [self.lblTest setUserInteractionEnabled:YES];
//        
//        NSLog(@"Adding UITapGestureRecognizer");
//        UITapGestureRecognizer *singleTap = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(handleSingleTap:)];
//        [self.lblTest addGestureRecognizer:singleTap];
//        [self.lblTest setUserInteractionEnabled:YES];
    }
    return self;
}


- (void)setSelected:(BOOL)selected animated:(BOOL)animated
{
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}

@end
